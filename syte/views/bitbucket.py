# -*- coding: utf-8 -*-
import requests
import json
from operator import itemgetter

from django.http import HttpResponse
from django.conf import settings


def bitbucket(request, username):
    r = requests.get('{0}users/{1}/'.format(
        settings.BITBUCKET_API_URL, username))

    data = r.json()

    # Number of followers
    r_followers = requests.get('{0}users/{1}/followers/'.format(
        settings.BITBUCKET_API_URL, username))
    data['user']['followers'] = r_followers.json()['count']

    # Count public repositories
    data['user']['public_repos'] = len(data['repositories'])

    for repo in data['repositories']:
        repo['language'] = repo['language'].capitalize()

        # Get number of forks
        if settings.BITBUCKET_SHOW_FORKS:
            r_forks = requests.get('{0}repositories/{1}/{2}'.format(
                settings.BITBUCKET_API_URL,
                username,
                repo['slug']))
            repo['forks_count'] = r_forks.json()['forks_count']

    # Sort the repositories on utc_last_updated
    data['repositories'].sort(key=itemgetter('utc_last_updated'), reverse=True)

    return HttpResponse(content=json.dumps(data), status=r.status_code,
                        content_type=r.headers['content-type'])
