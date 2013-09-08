# -*- coding: utf-8 -*-
import json
from linkedin import linkedin

from django.http import HttpResponse
from django.conf import settings


def linkedin_view(request):
    authentication = linkedin.LinkedInDeveloperAuthentication(
        consumer_key=settings.LINKEDIN_CONSUMER_KEY,
        consumer_secret=settings.LINKEDIN_CONSUMER_SECRET,
        user_token=settings.LINKEDIN_USER_TOKEN,
        user_secret=settings.LINKEDIN_USER_SECRET,
        redirect_uri=settings.SITE_ROOT_URI,
        permissions=linkedin.PERMISSIONS.enums.values()
    )

    application = linkedin.LinkedInApplication(authentication)
    profile_data = application.get_profile(selectors=['id', 'first-name', 'last-name', 'headline', 'location',
                                                      'num-connections', 'skills', 'educations', 'picture-url',
                                                      'site-standard-profile-request', 'summary', 'positions',
                                                      'industry'])
    group_data = application.get_memberships()
    network_updates_data = application.get_network_updates(types=settings.LINKEDIN_NETWORK_UPDATE_TYPES)

    context = {'profile': profile_data, 'groups': group_data, 'network_updates': network_updates_data}

    return HttpResponse(content=json.dumps(context),
                        status=200,
                        content_type='application/json')
