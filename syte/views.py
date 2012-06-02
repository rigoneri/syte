
from context_processor import site_pages
from django.shortcuts import redirect, render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.conf import settings

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
    r = requests.get('{0}/posts?api_key={1}'.format(settings.TUMBLR_API_URL, 
        settings.TUMBLR_API_KEY))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog_post(request, post_id):
    if request.is_ajax():
        r = requests.get('{0}/posts?api_key={1}&id={2}'.format(settings.TUMBLR_API_URL,
            settings.TUMBLR_API_KEY, post_id))
        return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])

    return render(request, 'index.html', {'post_id': post_id})


def blog_tags(request, tag_slug):
    #Due to the issue with the tumblr api described below we will redirect to the
    #users tumblr tags page for now.
    return redirect('http://{0}/tagged/{1}'.format(
        settings.TUMBLR_BLOG_URL, tag_slug))

    if request.is_ajax():
        #Important!!! This request doesn't work for now. There is a bug filed with
        #tumblr where the array of posts are always being returned empty. For now I'll
        #point directly to tumblr's url.
        #https://groups.google.com/d/topic/tumblr-api/9KfQZPKqcgA/discussion
        r = requests.get('{0}/posts/text?api_key={1}&tag={2}'.format(settings.TUMBLR_API_URL,
                settings.TUMBLR_API_KEY, tag_slug))
        return HttpResponse(content=json.loads(r.text), status=r.status_code,
                content_type=r.headers['content-type'])

    return render(request, 'index.html', {'tag_slug': tag_slug})




