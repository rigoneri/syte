# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.conf import settings
from rauth.service import OAuth1Service


def twitter(request, username):
    twitter = OAuth1Service(
        name='twitter',
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        request_token_url=settings.TWITTER_API_URL + 'oauth/request_token',
        access_token_url=settings.TWITTER_API_URL + 'oauth/access_token',
        authorize_url=settings.TWITTER_API_URL + 'oauth/authorize',
        header_auth=True)

    url = '{0}1/statuses/user_timeline.json?include_rts=false' \
        '&exclude_replies=true&count=50&screen_name={1}'.format(
            settings.TWITTER_API_URL, username)

    r = twitter.request('GET', url, access_token=settings.TWITTER_USER_KEY,
                        access_token_secret=settings.TWITTER_USER_SECRET)

    return HttpResponse(content=json.dumps(r.response.json),
                        status=r.response.status_code,
                        content_type=r.response.headers['content-type'])
