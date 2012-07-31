
import os
import sys
import subprocess
import shlex
import traceback

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_before_site = path_to_here[0:path_to_here.rfind('syte')]
sys.path.append(path_before_site)
os.environ['DJANGO_SETTINGS_MODULE'] = 'syte.settings'

from django.conf import settings

def compress_statics():
    try:
        #This won't work on windows.
        subprocess.check_call(shlex.split('mkdir -p static/css static/js/min'))
    except Exception:
        print 'Make sure to create "syte > static > css" and "syte > static > js > min" before compressing statics.'

    compress_styles()
    compress_js()

def compress_styles():
    less_path = 'static/less/styles.less'
    css_path = 'static/css/'

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

    if settings.BITBUCKET_INTEGRATION_ENABLED:
        js_files.append('components/bitbucket.js')

    combined = ''
    for js in js_files:
        f = open('static/js/' + js, 'r')
        combined += f.read()
        f.close()

    f = open('static/js/combined.js', 'w')
    f.write(combined)
    f.close()

    try:
        subprocess.check_call(shlex.split('uglifyjs -o static/js/min/scripts-{0}.min.js static/js/combined.js'.format(settings.COMPRESS_REVISION_NUMBER)))
        subprocess.check_call(shlex.split('rm -f static/js/combined.js'))
        print 'JavaScript Combined and Minified: scripts-{0}.min.js'.format(settings.COMPRESS_REVISION_NUMBER)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stack_trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print stack_trace

if __name__ == "__main__":
    compress_statics()
    sys.exit()
