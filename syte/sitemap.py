#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import math

PATH_TO_HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PATH_TO_HERE, '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'syte.settings'

from django.conf import settings
from datetime import datetime


def generate_sitemap():
	print 'Generating sitemap with urls: {0}'.format(settings.SITE_ROOT_URI)

	r = requests.get('{0}/posts?api_key={1}'.format(
        settings.TUMBLR_API_URL, settings.TUMBLR_API_KEY))

	sitemap = '<?xml version="1.0" encoding="utf-8"?>'\
		'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
	posts = r.json['response']['posts']
	
	i = 1;
	t = 1.0;

	for post in posts:
		f_date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S %Z')
		if (i % 2) == 0:
			t -= 0.1
			if t < 0.1:
				t = 0.0

		sitemap += _add_url(post['id'], f_date.strftime('%Y-%m-%d'), t)
		i += 1

	sitemap += '</urlset>'

	with open(os.path.join(PATH_TO_HERE, 'templates/sitemap.xml'), 'w') as f:
		f.write(sitemap)

	print 'Done generating sitemap'

def _add_url(id, date, priority):
	return '<url><loc>{0}post/{1}</loc><lastmod>{2}</lastmod>' \
		'<changefreq>monthly</changefreq><priority>{3}</priority>'\
		'</url>'.format(settings.SITE_ROOT_URI, id, date, priority)

if __name__ == "__main__":
    generate_sitemap()
    sys.exit()