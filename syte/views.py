
from context_processor import site_pages
from django.shortcuts import redirect, render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.conf import settings
from datetime import datetime

import requests
import json
import oauth2 as oauth


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

    user_r = requests.get('{0}{1}'.format(settings.GITHUB_USER_API_URL, username))
    repos_r = requests.get('{0}{1}'.format(settings.GITHUB_REPOS_API_URL, username))

    context = json.loads(user_r.text)
    context.update(json.loads(repos_r.text))

    return HttpResponse(content=json.dumps(context), status=repos_r.status_code,
                        content_type=repos_r.headers['content-type'])


def dribbble(request, username):
    r = requests.get('{0}{1}/shots'.format(settings.DRIBBBLE_API_URL, username))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog(request):
    r = requests.get('{0}/posts/text?api_key={1}'.format(settings.TUMBLR_API_URL, 
        settings.TUMBLR_API_KEY))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog_post(request, post_id):
    r = requests.get('{0}/posts/text?api_key={1}&id={2}'.format(settings.TUMBLR_API_URL,
            settings.TUMBLR_API_KEY, post_id))
    return _render_blog_posts(request, r)


def blog_tags(request, tag_slug):

    #Important!!! This request doesn't work for now. There is a bug filed with
    #tumblr where the array of posts are always being returned empty. For now I'll
    #point directly to tumblr's url.
    #https://groups.google.com/d/topic/tumblr-api/9KfQZPKqcgA/discussion
    r = requests.get('{0}/posts/text?api_key={1}&tag={2}'.format(settings.TUMBLR_API_URL,
            settings.TUMBLR_API_KEY, tag_slug))

    print '{0}/posts/text?api_key={1}&tag={2}'.format(settings.TUMBLR_API_URL,
            settings.TUMBLR_API_KEY, tag_slug)
    return _render_blog_posts(request, r, tags=True)



def _render_blog_posts(request, r, tags=False):
    response = json.loads(r.text)
    status_code = response['meta']['status']
    if status_code != 200:
        raise Http404

    posts = response['response']['posts']
    for p in posts:
        date = datetime.strptime(p['date'], '%Y-%m-%d %H:%M:%S %Z')
        p['formated_date'] = date.strftime('%B %d, %Y')

    return render(request, 'post.html', {
        'posts': posts,
        'is_tag_view': tags
     })






