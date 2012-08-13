
from django.http import HttpResponse
from django.conf import settings

import requests
import json


def soundcloud(request, username):
    context = dict()
    user_profile = requests.get('{0}users/{1}.json?client_id={2}'.format(
        settings.SOUNDCLOUD_API_URL,
        username,
        settings.SOUNDCLOUD_CLIENT_ID))
    user_tracks = requests.get('{0}users/{1}/tracks.json?client_id={2}'.format(
        settings.SOUNDCLOUD_API_URL,
        username,
        settings.SOUNDCLOUD_CLIENT_ID))

    context = {
        'user_profile' : user_profile.json,
        'user_tracks' : {
            'tracks' : user_tracks.json,
            'show_artwork' : settings.SOUNDCLOUD_SHOW_ARTWORK,
            'player_color' : settings.SOUNDCLOUD_PLAYER_COLOR
        }
    }
    return HttpResponse(content=json.dumps(context), status=user_profile.status_code,
                        content_type=user_profile.headers['content-type'])


