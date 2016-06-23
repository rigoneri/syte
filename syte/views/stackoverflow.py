# -*- coding: utf-8 -*-
import json

import requests
from django.http import HttpResponse
from django.conf import settings


def stackoverflow(request, userid):
    user_r = requests.get('{0}users/{1}?site=stackoverflow&filter=!-*f(6q3e0kZX'.format(
        settings.STACKOVERFLOW_API_URL,
        userid))

    timeline_r = requests.get('{0}users/{1}/timeline?site=stackoverflow&filter=!))x30_N'.format(
        settings.STACKOVERFLOW_API_URL,
        userid))

    context = {'user': user_r.json()["items"][0]}
    context.update({'timeline': timeline_r.json()["items"]})

    return HttpResponse(content=json.dumps(context),
                        status=timeline_r.status_code,
                        content_type=timeline_r.headers['content-type'])
