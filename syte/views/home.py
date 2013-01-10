# -*- coding: utf-8 -*-
import requests

from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.conf import settings
from syte.context_processor import site_pages

def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))


def page_not_found_error(request, template_name='404.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseNotFound(t.render(Context(d)))


def home(request):
    context = dict()
    if request.GET.get('o', None):
        context['open_integration'] = request.GET['o']
    return render(request, 'index.html', context)

def rss(request):
	r = requests.get('{0}'.format(settings.RSS_FEED_URL))
	new_content = r.text.encode('utf-8').replace(settings.TUMBLR_BLOG_URL, settings.SITE_ROOT_URI[7:-1])

	return HttpResponse(content=new_content,
						status=r.status_code,
						content_type=r.headers['content-type'])
