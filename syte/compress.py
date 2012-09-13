#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shlex
import traceback

PATH_TO_HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PATH_TO_HERE, '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'syte.settings'

from django.conf import settings


def compress_statics():
    out_paths = (os.path.join(PATH_TO_HERE, 'static/css'),
                 os.path.join(PATH_TO_HERE, 'static/js/min'))

    try:
        for path in out_paths:
            if not os.path.exists(path):
                os.mkdir(path)
    except OSError:
        print 'Make sure to create "syte > static > css" and "syte > static > js > min" before compressing statics.'

    compress_styles()
    compress_js()


def compress_styles():
    less_path = os.path.join(PATH_TO_HERE, 'static/less/styles.less')
    css_path = os.path.join(PATH_TO_HERE, 'static/css/')

    try:
        subprocess.check_call(shlex.split('lessc {0} {1}styles-{2}.min.css -yui-compress'
            .format(less_path, css_path, settings.COMPRESS_REVISION_NUMBER)))
        print 'CSS Styles Generated: styles-{0}.min.css'.format(settings.COMPRESS_REVISION_NUMBER)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stack_trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print stack_trace


def compress_js():
    js_files = [
        'libs/jquery.url.js',
        'libs/require.js',
        'libs/handlebars.js',
        'libs/moment.min.js',
        'libs/bootstrap-modal.js',
        'libs/spin.min.js',
        'libs/prettify.js',

        'components/base.js',
        'components/mobile.js',
        'components/blog-posts.js',
        'components/links.js',
    ]

    if settings.TWITTER_INTEGRATION_ENABLED:
        js_files.append('components/twitter.js')

    if settings.GITHUB_INTEGRATION_ENABLED:
        js_files.append('components/github.js')

    if settings.DRIBBBLE_INTEGRATION_ENABLED:
        js_files.append('components/dribbble.js')

    if settings.INSTAGRAM_INTEGRATION_ENABLED:
        js_files.append('components/instagram.js')

    if settings.DISQUS_INTEGRATION_ENABLED:
        js_files.append('components/disqus.js')

    if settings.LASTFM_INTEGRATION_ENABLED:
        js_files.append('components/lastfm.js')

    if settings.SOUNDCLOUD_INTEGRATION_ENABLED:
        js_files.append('components/soundcloud.js')

    if settings.BITBUCKET_INTEGRATION_ENABLED:
        js_files.append('components/bitbucket.js')

    if settings.FOURSQUARE_INTEGRATION_ENABLED:
        js_files.append('components/foursquare.js')

    combined = ''
    for js in js_files:
        with open(os.path.join(PATH_TO_HERE, 'static/js/' + js), 'r') as f:
            combined += f.read()

    with open(os.path.join(PATH_TO_HERE, 'static/js/combined.js'), 'w') as f:
        f.write(combined)

    try:
        subprocess.check_call(shlex.split('uglifyjs -o {0}scripts-{1}.min.js {2}'.format(
            os.path.join(PATH_TO_HERE, 'static/js/min/'),
            settings.COMPRESS_REVISION_NUMBER,
            os.path.join(PATH_TO_HERE, 'static/js/combined.js'))))
        os.remove(os.path.join(PATH_TO_HERE, 'static/js/combined.js'))
        print 'JavaScript Combined and Minified: scripts-{0}.min.js'.format(settings.COMPRESS_REVISION_NUMBER)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stack_trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print stack_trace


if __name__ == "__main__":
    compress_statics()
    sys.exit()
