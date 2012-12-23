# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings


handler404 = 'syte.views.home.page_not_found_error'
handler500 = 'syte.views.home.server_error'

urlpatterns = patterns('',
    url(r'^post/(?P<post_id>\w+)/?$', 'syte.views.blog.blog_post'),
    url(r'^tags/(?P<tag_slug>[\s\w\d-]+)/?$', 'syte.views.blog.blog_tags'),
    url(r'^blog.json/?$', 'syte.views.blog.blog'),
    url(r'^about/?$', 'syte.views.home.home'),
    url(r'^/?$', 'syte.views.home.home'),
)

#Twitter Integration
if settings.TWITTER_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^twitter/(?P<username>\w+)/?$', 'syte.views.twitter.twitter'),
    )

#Github Integration
if settings.GITHUB_OAUTH_ENABLED:
    urlpatterns += patterns('',
        url(r'^github/auth/?$', 'syte.views.github.github_auth'),
    )

if settings.GITHUB_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^github/(?P<username>[\-\w]+)/?$', 'syte.views.github.github'),
    )

#Bitbucket Integration
if settings.BITBUCKET_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^bitbucket/(?P<username>\w+)/?$', 'syte.views.bitbucket.bitbucket'),
    )

#Dribbble Integration
if settings.DRIBBBLE_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^dribbble/(?P<username>\w+)/?$', 'syte.views.dribbble.dribbble'),
    )

#Instagram Integration
if settings.FOURSQUARE_OAUTH_ENABLED:
    urlpatterns += patterns('',
        url(r'^foursquare/auth/?$', 'syte.views.foursquare.foursquare_auth'),
    )

if settings.FOURSQUARE_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^foursquare/?$', 'syte.views.foursquare.foursquare'),
    )

#Foursquare Integration
if settings.INSTAGRAM_OAUTH_ENABLED:
    urlpatterns += patterns('',
        url(r'^instagram/auth/?$', 'syte.views.instagram.instagram_auth'),
    )

if settings.INSTAGRAM_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^instagram/(?P<max_id>\w+)/?$', 'syte.views.instagram.instagram_next'),
        url(r'^instagram/?$', 'syte.views.instagram.instagram'),
    )

#LastFM Integration
if settings.LASTFM_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^lastfm/(?P<username>\S+)/?$', 'syte.views.lastfm.lastfm'),
    )

#Soundcloud Integration
if settings.SOUNDCLOUD_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^soundcloud/(?P<username>\S+)/?$', 'syte.views.soundcloud.soundcloud'),
    )

#Statics: Hacky for now... fix this later...
urlpatterns += patterns('',
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '/static/imgs/favicon.ico'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
