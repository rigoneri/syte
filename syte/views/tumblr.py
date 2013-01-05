# -*- coding: utf-8 -*-
import os
from datetime import datetime

import requests
import re, htmlentitydefs
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from pybars import Compiler


def blog(request):
    offset = request.GET.get('o', 0)
    r = requests.get('{0}/posts?api_key={1}&offset={2}'.format(
        settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, offset))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])


def blog_post(request, post_id):
    context = dict()

    r = requests.get('{0}/posts?api_key={1}&id={2}'.format(
        settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, post_id))

    if r.status_code == 200:
        post_response = r.json.get('response', {})
        posts = post_response.get('posts', [])

        if posts:
            post = posts[0]
            f_date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S %Z')
            post['formated_date'] = f_date.strftime('%B %d, %Y')

            if settings.DISQUS_INTEGRATION_ENABLED:
                post['disqus_enabled'] = True
            if settings.SHARETHIS_PUBLISHER_KEY:
                post['sharethis_enabled'] = True

            path = '{0}/static/templates/blog-post-{1}.html'.format(
                os.path.join(os.path.dirname(__file__), '..'), post['type'])
            with open(path, 'r') as f:
                f_data = f.read()

            compiler = Compiler()
            template = compiler.compile(unicode(f_data))
            context['post_data'] = template(post)

            alt_title = ''
            if (post['type'] == 'photo' or post['type'] == 'video'):
                alt_title = '{0}: {1}'.format(post['type'].capitalize(), post['caption'][3:-4])
            elif (post['type'] == 'quote'):
                alt_title = '{0}: {1}'.format(post['type'].capitalize(), post['text'])
            elif (post['type'] == 'audio'):
                alt_title = '{0}: {1} - {2}'.format(post['type'].capitalize(), post['artist'], post['track_name'])

            context['post_title'] = post.get('title', unescape(alt_title))

    return render(request, 'blog-post.html', context)


def blog_tags(request, tag_slug):
    offset = request.GET.get('o', 0)
    if request.is_ajax():
        r = requests.get('{0}/posts?api_key={1}&tag={2}&offset={3}'.format(
            settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY, tag_slug.encode('UTF-8'), offset))
        return HttpResponse(content=r.text, status=r.status_code,
                            content_type=r.headers['content-type'])
    return render(request, 'index.html', {'tag_slug': tag_slug})

## Thanks to Fredrik Lundh for this function (http://effbot.org/zone/re-sub.htm#unescape-html)
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
