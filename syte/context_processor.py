
from django.conf import settings

def site_pages(request):
    context = dict()
    if settings.DEPLOYMENT_MODE == 'dev':
        context['DEV_DEPLOYMENT_MODE'] = True

    context['COMPRESS_REVISION_NUMBER'] = settings.COMPRESS_REVISION_NUMBER
    context['MEDIA_URL'] = settings.MEDIA_URL

    context['TWITTER_INTEGRATION_ENABLED'] = settings.TWITTER_INTEGRATION_ENABLED
    context['GITHUB_INTEGRATION_ENABLED'] = settings.GITHUB_INTEGRATION_ENABLED
    context['DRIBBBLE_INTEGRATION_ENABLED'] = settings.DRIBBBLE_INTEGRATION_ENABLED
    context['INSTAGRAM_INTEGRATION_ENABLED'] = settings.INSTAGRAM_INTEGRATION_ENABLED

    return context
