# -*- coding: utf-8 -*-
import json

import requests
from django.http import HttpResponse
from django.conf import settings


def lastfm(request, username):
    url = '{0}?method=user.getrecenttracks&user={1}&api_key={2}&format=json'.format(
        settings.LASTFM_API_URL, username, settings.LASTFM_API_KEY)
    tracks = requests.get(url)

    url = '{0}?method=user.getinfo&user={1}&api_key={2}&format=json'.format(
        settings.LASTFM_API_URL, username, settings.LASTFM_API_KEY)
    user = requests.get(url)

    context = {
        'user_info': user.json,
        'recenttracks': tracks.json,
    }

    return HttpResponse(content=json.dumps(context), status=user.status_code,
                        content_type=user.headers['content-type'])
