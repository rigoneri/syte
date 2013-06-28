# -*- coding: utf-8 -*-
import json
import twitter

from django.http import HttpResponse
from django.conf import settings

def twitter_view(request, username):
    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                      consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                      access_token_key=settings.TWITTER_USER_KEY,
                      access_token_secret=settings.TWITTER_USER_SECRET)

    statuses = api.GetUserTimeline(username, include_rts=True, 
        exclude_replies=True, count=50)

    statuses_in_dict = []
    for s in statuses:
        statuses_in_dict.append(json.loads(s.AsJsonString()))

    return HttpResponse(content=json.dumps(statuses_in_dict),
                        status=200,
                        content_type='application/json')