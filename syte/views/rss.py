# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse
from django.conf import settings

def rss(request):
	r = requests.get('{0}'.format(settings.RSS_FEED_URL))
	new_url = r.text.encode('utf-8').replace(settings.TUMBLR_BLOG_URL, settings.SITE_ROOT_URI[7:-1])

	return HttpResponse(content=new_url,
						status=r.status_code,
						content_type=r.headers['content-type'])
