# -*- coding: utf-8 -*-
import os
import re
import htmlentitydefs
import requests

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
from pybars import Compiler
from HTMLParser import HTMLParser


# Takes a response (e.g. from Wordpress) and converts it into a format that
# will be accepted by the Handlebars templates
def convertWordpressResponse(post):
    post['id'] = post['ID']
    post['body'] = post['content']
    post['tags'] = []

    date = post['date']
    pos = date.rfind('+')
    if pos > 0:
        date = date[0:pos]
    else:
        pos = date.rfind('-')
        date = date[0:pos]
    f_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    post['formated_date'] = f_date.strftime('%B %d, %Y')

    if post['type'] == 'post':
        post['type'] = 'text'


def blog(request):
    offset = request.GET.get('o', 0)
    r = requests.get('{0}/posts?api_key={1}&offset={2}'.format(
        settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, offset))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog_post(request, post_id):
    if settings.BLOG_PLATFORM == 'tumblr':
        r = requests.get('{0}/posts?api_key={1}&id={2}'.format(
            settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, post_id))

        if r.status_code == 200:
            post_response = r.json().get('response', {})
            posts = post_response.get('posts', [])

            if posts:
                post = posts[0]
                f_date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S %Z')
                post['formated_date'] = f_date.strftime('%B %d, %Y')

    elif settings.BLOG_PLATFORM == 'wordpress':
        r = requests.get('{0}/posts/{1}'.format(
            settings.WORDPRESS_API_URL, post_id))
        if r.status_code == 200:
            # Get Wordpress response into the same format as Tumblr so we can
            # reuse Handlebars template
            post = r.json()
            convertWordpressResponse(post)

    # At this point we should have a post dict from either Tumblr or Wordpress
    post['disqus_enabled'] = settings.DISQUS_INTEGRATION_ENABLED
    if settings.SHARETHIS_PUBLISHER_KEY:
        post['sharethis_enabled'] = True

    path = '{0}/static/templates/blog-post-{1}.html'.format(
        os.path.join(os.path.dirname(__file__), '..'), post['type'])
    with open(path, 'r') as f:
        f_data = f.read()

    compiler = Compiler()
    template = compiler.compile(unicode(f_data))

    context = dict()
    context['post_data'] = template(post)

    alt_title = ''
    if (post['type'] == 'photo' or post['type'] == 'video'):
        alt_title = '{0}: {1}'.format(post['type'].capitalize(), post['caption'][3:-4])
    elif (post['type'] == 'quote'):
        alt_title = '{0}: {1}'.format(post['type'].capitalize(), post['text'])
    elif (post['type'] == 'audio'):
        alt_title = '{0}: {1} - {2}'.format(post['type'].capitalize(), post['artist'], post['track_name'])

    context['post_title'] = post.get('title', unescape(alt_title))

    if post['type'] == 'text' and post['body']:
        context['meta_description'] = strip_tags(post['body'])[:150]

    if post['tags']:
        context['meta_keywords'] = ', '.join(post['tags'])

    return render(request, 'blog-post.html', context)


def blog_tags(request, tag_slug):
    offset = request.GET.get('o', 0)

    if request.is_ajax():
        if settings.BLOG_PLATFORM == 'tumblr':
            r = requests.get('{0}/posts?api_key={1}&tag={2}&offset={3}'.format(
                settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, tag_slug.encode('UTF-8'), offset))
            return HttpResponse(content=r.text, status=r.status_code,
                                content_type=r.headers['content-type'])

        elif settings.BLOG_PLATFORM == 'wordpress':
            r = requests.get('{0}/posts?tag={1}&offset={2}'.format(
                settings.WORDPRESS_API_URL, settings.TUMBLR_API_KEY, tag_slug.encode('UTF-8'), offset))
            if r.status_code == 200:
                convertWordpressResponse(r.json())
            return HttpResponse(content=r.text, status=r.status_code,
                              content_type=r.headers['content-type'])

    # Non-ajax request
    return render(request, 'index.html', {'tag_slug': tag_slug})


# Thanks to Fredrik Lundh for this function (http://effbot.org/zone/re-sub.htm#unescape-html)
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text
    return re.sub("&#?\w+;", fixup, text)


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
