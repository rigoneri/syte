# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse
from django.conf import settings


def dribbble(request, username):
    r = requests.get('{0}{1}/shots'.format(settings.DRIBBBLE_API_URL, username))
    return HttpResponse(content=r.text, status=r.status_code,
                        content_type=r.headers['content-type'])
