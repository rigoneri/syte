# -*- coding: utf-8 -*-
import json
from operator import itemgetter
from xml.etree import ElementTree

import requests
from django.conf import settings
from django.http import HttpResponse

from syte.views.home import server_error


def ohloh(request, username):
    r = requests.get('{0}accounts/{1}.xml?api_key={2}'.format(
        settings.OHLOH_API_URL, username, settings.OHLOH_API_KEY))

    root = ElementTree.fromstring(r.text)

    # Error handling
    error = root.find('error')
    if error is not None:
        print "Ohloh error:", error.text
        return server_error(requests)

    # Basic account information
    account = root.find('result/account')
    context = {node.tag: node.text for node in account}
    context['position'] = account.find('kudo_score/position').text
    context['kudo_score'] = account.find('kudo_score/kudo_rank').text

    # Accounts language experiences
    total_commits = 0
    total_lines = 0
    context['languages'] = []
    for node in account.find('languages'):
        values = {i.tag: i.text for i in node}

        # Language experience prettify output
        years = int(values['experience_months']) // 12
        months = int(values['experience_months']) % 12
        if years:
            values['experience'] = '%iy %im' % (years, months)
        else:
            values['experience'] = '%im' % months

        values['name'] = values['name'].capitalize()
        context['languages'].append(values)

        total_commits += int(values['total_commits'].replace(',', ''))
        total_lines += int(values['total_lines_changed'].replace(',', ''))

    context['total_languages'] = len(context['languages'])
    context['total_commits'] = total_commits
    context['total_lines_changed'] = total_lines

    # Project managed by 'username'
    man_r = requests.get('{0}accounts/{1}/projects.xml?api_key={2}'.format(
        settings.OHLOH_API_URL, username, settings.OHLOH_API_KEY))
    root = ElementTree.fromstring(man_r.text)
    context['projects'] = [{i.tag: i.text for i in node}
                           for node in root.find('result')]
    context['managed_projects'] = len(context['projects'])

    # Other projects 'username' has contributed to
    for name in settings.OHLOH_OTHER_PROJECTS:
        pro_r = requests.get('{0}p/{1}.xml?api_key={2}'.format(
            settings.OHLOH_API_URL, name, settings.OHLOH_API_KEY))
        root = ElementTree.fromstring(pro_r.text)
        values = {i.tag: i.text for i in root.find('result/project')}
        context['projects'].append(values)

    context['total_projects'] = len(context['projects'])
    context['projects'].sort(key=itemgetter('name'))

    return HttpResponse(json.dumps(context),
                        'application/json; charset=utf-8', r.status_code)
