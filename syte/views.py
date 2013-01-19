
from context_processor import site_pages
from django.shortcuts import redirect, render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.conf import settings
from pybars import Compiler
from datetime import datetime

import os
import requests
import json
import oauth2 as oauth
from utils import slugify


def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))

def page_not_found_error(request, template_name='404.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))


def home(request):
    return render(request, 'index.html', {})


def twitter(request, username):
    consumer = oauth.Consumer(key=settings.TWITTER_CONSUMER_KEY,
            secret=settings.TWITTER_CONSUMER_SECRET)
    token = oauth.Token(key=settings.TWITTER_USER_KEY,
            secret=settings.TWITTER_USER_SECRET)
    client = oauth.Client(consumer, token)

    resp, content = client.request(
        '{0}{1}'.format(settings.TWITTER_API_URL, username),
        method = 'GET',
        headers = None,
        force_auth_header=True
    )

    return HttpResponse(content=content, status=resp.status,
             content_type=resp['content-type'])

def github(request, username):
    user_r = requests.get('{0}users/{1}?access_token={2}'.format(
        settings.GITHUB_API_URL,
        username,
        settings.GITHUB_ACCESS_TOKEN))

    repos_r = requests.get('{0}users/{1}/repos?access_token={2}'.format(
        settings.GITHUB_API_URL,
        username,
        settings.GITHUB_ACCESS_TOKEN))

    context = {'user': user_r.json}
    context.update({'repos': repos_r.json})

    return HttpResponse(content=json.dumps(context), status=repos_r.status_code,
                        content_type=repos_r.headers['content-type'])

def github_auth(request):
    context = dict()
    code = request.GET.get('code', None)
    error = request.GET.get('error_description', None)

    if not code and not error:
        return redirect('{0}?client_id={1}&redirect_uri={2}github/auth/&response_type=code'.format(
            settings.GITHUB_OAUTH_AUTHORIZE_URL,
            settings.GITHUB_CLIENT_ID,
            settings.SITE_ROOT_URI))

    if code:
        r = requests.post(settings.GITHUB_OAUTH_ACCESS_TOKEN_URL, data = {
              'client_id': settings.GITHUB_CLIENT_ID,
              'client_secret': settings.GITHUB_CLIENT_SECRET,
              'redirect_uri': '{0}github/auth/'.format(settings.SITE_ROOT_URI),
              'code': code,
            }, headers={'Accept': 'application/json'});

        try:
            data = r.json
            error = data.get('error', None)
        except:
            error = r.text

        if not error:
            context['token'] = data['access_token']

    if error:
        context['error'] = error

    return render(request, 'github_auth.html', context)


def dribbble(request, username):
    r = requests.get('{0}{1}/shots'.format(settings.DRIBBBLE_API_URL, username))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog(request):
    offset = request.GET.get('o', 0)
    r = requests.get('{0}/posts?api_key={1}&offset={2}'.format(settings.TUMBLR_API_URL,
        settings.TUMBLR_API_KEY, offset))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog_post(request, post_id):
    context = dict()

    r = requests.get('{0}/posts?api_key={1}&id={2}'.format(settings.TUMBLR_API_URL,
            settings.TUMBLR_API_KEY, post_id))

    if r.status_code == 200:
        post_response = r.json.get('response', {})
        posts = post_response.get('posts', [])

        if posts:
            post = posts[0]
            f_date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S %Z')
            post['formated_date'] = f_date.strftime('%B %d, %Y')

            if settings.DISQUS_INTEGRATION_ENABLED:
                post['disqus_enabled'] = True

            path_to_here = os.path.abspath(os.path.dirname(__file__))
            f = open('{0}/static/templates/blog-post-{1}.html'.format(path_to_here, post['type']), 'r')
            f_data = f.read()
            f.close()

            compiler = Compiler()
            template = compiler.compile(unicode(f_data))
            context['post_data'] = template(post)
            context['post_title'] = post.get('title', None)

    return render(request, 'blog-post.html', context)


def blog_tags(request, tag_slug):
    offset = request.GET.get('o', 0)
    if request.is_ajax():
        r = requests.get('{0}/posts?api_key={1}&tag={2}&offset={3}'.format(settings.TUMBLR_API_URL, 
            settings.TUMBLR_API_KEY, tag_slug, offset))
        return HttpResponse(content=r.text, status=r.status_code,
                content_type=r.headers['content-type'])
    return render(request, 'index.html', {'tag_slug': tag_slug})


def instagram_auth(request):
    context = dict()
    code = request.GET.get('code', None)
    error = request.GET.get('error_description', None)

    if not code and not error:
        return redirect('{0}?client_id={1}&redirect_uri={2}instagram/auth/&response_type=code'.format(
            settings.INSTAGRAM_OAUTH_AUTHORIZE_URL,
            settings.INSTAGRAM_CLIENT_ID,
            settings.SITE_ROOT_URI))

    if code:
        r = requests.post(settings.INSTAGRAM_OAUTH_ACCESS_TOKEN_URL, data = {
              'client_id': settings.INSTAGRAM_CLIENT_ID,
              'client_secret': settings.INSTAGRAM_CLIENT_SECRET,
              'grant_type': 'authorization_code',
              'redirect_uri': '{0}instagram/auth/'.format(settings.SITE_ROOT_URI),
              'code': code,
            });

        data = json.loads(r.text)
        error = data.get('error_message', None)

        if not error:
            context['token'] = data['access_token']
            context['user_id'] = data['user'].get('id', None)
            context['user_name'] = data['user'].get('full_name', None)

    if error:
        context['error'] = error

    return render(request, 'instagram_auth.html', context)



def instagram(request):
    user_r = requests.get('{0}users/{1}/?access_token={2}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN))
    user_data = json.loads(user_r.text)

    media_r = requests.get('{0}users/{1}/media/recent/?access_token={2}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN))
    media_data = json.loads(media_r.text)

    context = {
        'user': user_data.get('data', None),
        'media': media_data.get('data', None),
        'pagination': media_data.get('pagination', None),
        }

    return HttpResponse(content=json.dumps(context), status=media_r.status_code,
                        content_type=media_r.headers['content-type'])


def instagram_next(request, max_id):
    media_r = requests.get('{0}users/{1}/media/recent/?access_token={2}&max_id={3}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN,
        max_id))
    media_data = json.loads(media_r.text)

    context = {
        'media': media_data.get('data', None),
        'pagination': media_data.get('pagination', None),
    }

    return HttpResponse(content=json.dumps(context), status=media_r.status_code,
                        content_type=media_r.headers['content-type'])


def lastfm(request, username):
    url = '{0}?method=user.getrecenttracks&user={1}&api_key={2}&format=json'.format(
                                                    settings.LASTFM_API_URL,
                                                    settings.LASTFM_USERNAME,
                                                    settings.LASTFM_API_KEY)
    tracks = requests.get(url)
    url = '{0}?method=user.getinfo&user={1}&api_key={2}&format=json'.format(
                                                    settings.LASTFM_API_URL,
                                                    settings.LASTFM_USERNAME,
                                                    settings.LASTFM_API_KEY)
    user = requests.get(url)
    context = {
        'user_info': user.json,
        'recenttracks': tracks.json,
    }

    return HttpResponse(content=json.dumps(context), status=user.status_code,
                        content_type=user.headers['content-type'])

