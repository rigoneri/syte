
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

import requests
import json
import datetime

def foursquare_auth(request):
    context = dict()
    code = request.GET.get('code', None)
    error = request.GET.get('error', None)

    if not code and not error:
        return redirect('{0}?client_id={1}&redirect_uri={2}foursquare/auth/&response_type=code'.format(
            settings.FOURSQUARE_OAUTH_AUTHORIZE_URL,
            settings.FOURSQUARE_CLIENT_ID,
            settings.SITE_ROOT_URI))

    if code:
        r = requests.post(settings.FOURSQUARE_OAUTH_ACCESS_TOKEN_URL, data = {
              'client_id': settings.FOURSQUARE_CLIENT_ID,
              'client_secret': settings.FOURSQUARE_CLIENT_SECRET,
              'grant_type': 'authorization_code',
              'redirect_uri': '{0}foursquare/auth/'.format(settings.SITE_ROOT_URI),
              'code': code,
            })

        data = json.loads(r.text)
        error = data.get('error', None)

        if not error:
            context['token'] = data['access_token']

    if error:
        context['error'] = error

    return render(request, 'foursquare_auth.html', context)


def foursquare(request):
    user_r = requests.get('{0}users/self?oauth_token={1}&v=20120812'.format(
        settings.FOURSQUARE_API_URL,
        settings.FOURSQUARE_ACCESS_TOKEN))

    user_data = json.loads(user_r.text)
    user_response = user_data.get('response', {})
    user_info = user_response.get('user', None)

    checkins_r = requests.get('{0}users/self/checkins?oauth_token={1}&v=20120812'.format(
        settings.FOURSQUARE_API_URL,
        settings.FOURSQUARE_ACCESS_TOKEN))

    checkins_data = json.loads(checkins_r.text)
    checkins_response = checkins_data.get('response', {})
    checkins = checkins_response.get('checkins', None)

    if settings.FOURSQUARE_SHOW_CURRENT_DAY == False:
        valid_checkins = []
        now = datetime.datetime.now();
        for c in checkins['items']:
            created_at = c.get('createdAt', None)
            if created_at:
                created_at_dt = datetime.datetime.fromtimestamp(int(created_at))
                if (now - created_at_dt) > datetime.timedelta(days = 1):
                    valid_checkins.append(c)
        checkins['items'] = valid_checkins

    context = {
        'user': user_info,
        'checkins': checkins,
        }

    return HttpResponse(content=json.dumps(context), status=checkins_r.status_code,
                        content_type=checkins_r.headers['content-type'])

