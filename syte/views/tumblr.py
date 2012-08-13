
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
from pybars import Compiler

import os
import requests
import json


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
            settings.TUMBLR_API_KEY, tag_slug.encode('UTF-8'), offset))
        return HttpResponse(content=r.text, status=r.status_code,
                content_type=r.headers['content-type'])
    return render(request, 'index.html', {'tag_slug': tag_slug})

