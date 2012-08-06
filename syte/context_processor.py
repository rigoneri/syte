
from django.conf import settings

def site_pages(request):
    context = dict()
    if settings.DEPLOYMENT_MODE == 'dev':
        context['DEV_DEPLOYMENT_MODE'] = True

    context['COMPRESS_REVISION_NUMBER'] = settings.COMPRESS_REVISION_NUMBER
    context['MEDIA_URL'] = settings.MEDIA_URL

    context['RSS_FEED_URL'] = settings.RSS_FEED_URL
    context['RSS_FEED_ENABLED'] = settings.RSS_FEED_ENABLED

    context['TWITTER_INTEGRATION_ENABLED'] = settings.TWITTER_INTEGRATION_ENABLED
    context['GITHUB_INTEGRATION_ENABLED'] = settings.GITHUB_INTEGRATION_ENABLED
    context['DRIBBBLE_INTEGRATION_ENABLED'] = settings.DRIBBBLE_INTEGRATION_ENABLED
    context['INSTAGRAM_INTEGRATION_ENABLED'] = settings.INSTAGRAM_INTEGRATION_ENABLED

    context['DISQUS_INTEGRATION_ENABLED'] = settings.DISQUS_INTEGRATION_ENABLED
    context['DISQUS_SHORTNAME'] = settings.DISQUS_SHORTNAME

    context['LASTFM_INTEGRATION_ENABLED'] = settings.LASTFM_INTEGRATION_ENABLED
    context['SOUNDCLOUD_INTEGRATION_ENABLED'] = settings.SOUNDCLOUD_INTEGRATION_ENABLED

    context['GOOGLE_ANALYTICS_TRACKING_ID'] = settings.GOOGLE_ANALYTICS_TRACKING_ID

    return context
