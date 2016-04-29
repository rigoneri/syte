# -*- coding: utf-8 -*-

import json
import requests
from django.http import HttpResponse
from django.conf import settings

def dribbble(request, username):
    user_r = requests.get('{0}users/{1}?access_token={2}'.format(
        settings.DRIBBBLE_API_URL,
        username,
        settings.DRIBBBLE_ACCESS_TOKEN))

    shots_r = requests.get('{0}users/{1}/shots?access_token={2}'.format(
        settings.DRIBBBLE_API_URL,
        username,
        settings.DRIBBBLE_ACCESS_TOKEN))

    context = {'user': user_r.json()}
    context.update({'shots': shots_r.json()})

    return HttpResponse(content=json.dumps(context), 
                        status=shots_r.status_code,
                        content_type=shots_r.headers['content-type'])
