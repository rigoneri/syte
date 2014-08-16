# -*- coding: utf-8 -*-
import json
from linkedin import linkedin

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render

LINKEDIN_NETWORK_UPDATE_TYPES = linkedin.NETWORK_UPDATES.enums.values()

def linkedin_auth(request):
    code = request.GET.get('code', None)

    authentication = linkedin.LinkedInAuthentication(
        settings.LINKEDIN_API_KEY,
        settings.LINKEDIN_API_SECRET,
        '{0}linkedin/auth/'.format(settings.SITE_ROOT_URI),
        linkedin.PERMISSIONS.enums.values()
    )

    if not code:
        return redirect(authentication.authorization_url)

    if code:
        authentication.authorization_code = code
        token = authentication.get_access_token()
        return render(request, 'linkedin_auth.html', {'token': token[0]})

def linkedin_view(request):
    application = linkedin.LinkedInApplication(token=settings.LINKEDIN_TOKEN)
    profile_data = application.get_profile(selectors=['id', 'first-name', 'last-name', 'headline', 'location',
                                                      'num-connections', 'skills', 'educations', 'picture-url',
                                                      'site-standard-profile-request', 'summary', 'positions',
                                                      'industry'])
    group_data = application.get_memberships()
    network_updates_data = application.get_network_updates(types=LINKEDIN_NETWORK_UPDATE_TYPES)

    context = {'profile': profile_data, 'groups': group_data, 'network_updates': network_updates_data}

    return HttpResponse(content=json.dumps(context),
                        status=200,
                        content_type='application/json')
