
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

import requests
import json



def instagram_auth(request):
    context = dict()
    code = request.GET.get('code', None)
    error = request.GET.get('error_description', None)

    if not code and not error:
        return redirect('{0}?client_id={1}&redirect_uri={2}instagram/auth/&response_type=code'.format(
            settings.INSTAGRAM_OAUTH_AUTHORIZE_URL,
            settings.INSTAGRAM_CLIENT_ID,
            settings.SITE_ROOT_URI))

    if code:
        r = requests.post(settings.INSTAGRAM_OAUTH_ACCESS_TOKEN_URL, data = {
              'client_id': settings.INSTAGRAM_CLIENT_ID,
              'client_secret': settings.INSTAGRAM_CLIENT_SECRET,
              'grant_type': 'authorization_code',
              'redirect_uri': '{0}instagram/auth/'.format(settings.SITE_ROOT_URI),
              'code': code,
            })

        data = json.loads(r.text)
        error = data.get('error_message', None)

        if not error:
            context['token'] = data['access_token']
            context['user_id'] = data['user'].get('id', None)
            context['user_name'] = data['user'].get('full_name', None)

    if error:
        context['error'] = error

    return render(request, 'instagram_auth.html', context)



def instagram(request):
    user_r = requests.get('{0}users/{1}/?access_token={2}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN))
    user_data = json.loads(user_r.text)

    media_r = requests.get('{0}users/{1}/media/recent/?access_token={2}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN))
    media_data = json.loads(media_r.text)

    context = {
        'user': user_data.get('data', None),
        'media': media_data.get('data', None),
        'pagination': media_data.get('pagination', None),
        }

    return HttpResponse(content=json.dumps(context), status=media_r.status_code,
                        content_type=media_r.headers['content-type'])


def instagram_next(request, max_id):
    media_r = requests.get('{0}users/{1}/media/recent/?access_token={2}&max_id={3}'.format(
        settings.INSTAGRAM_API_URL,
        settings.INSTAGRAM_USER_ID,
        settings.INSTAGRAM_ACCESS_TOKEN,
        max_id))
    media_data = json.loads(media_r.text)

    context = {
        'media': media_data.get('data', None),
        'pagination': media_data.get('pagination', None),
    }

    return HttpResponse(content=json.dumps(context), status=media_r.status_code,
                        content_type=media_r.headers['content-type'])

