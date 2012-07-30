from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.conf import settings

handler404 = 'syte.views.page_not_found_error'
handler500 = 'syte.views.server_error'

urlpatterns = patterns('',
    url(r'^post/(?P<post_id>\w+)/?$', 'syte.views.blog_post'),
    url(r'^tags/(?P<tag_slug>\w+)/?$', 'syte.views.blog_tags'),
    url(r'^blog.json/?$', 'syte.views.blog'),
    url(r'^blog.pagination.json/(?P<tumblr_offset>\w+)/?$', 'syte.views.pagination'),
    
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", mimetype="text/plain")),
    url(r'^about/?$', 'syte.views.home'),
    url(r'^/?$', 'syte.views.home'),
)

#Twitter Integration
if settings.TWITTER_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^twitter/(?P<username>\w+)/?$', 'syte.views.twitter'),
    )

#Github Integration
if settings.GITHUB_OAUTH_ENABLED:
    urlpatterns += patterns('',
        url(r'^github/auth/?$', 'syte.views.github_auth'),
    )

if settings.GITHUB_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^github/(?P<username>\w+)/?$', 'syte.views.github'),
    )


#Dribbble Integration
if settings.DRIBBBLE_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^dribbble/(?P<username>\w+)/?$', 'syte.views.dribbble'),
    )

#Instagram Oauth
if settings.INSTAGRAM_OAUTH_ENABLED:
    urlpatterns += patterns('',
        url(r'^instagram/auth/?$', 'syte.views.instagram_auth'),
    )

if settings.INSTAGRAM_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^instagram/(?P<max_id>\w+)/?$', 'syte.views.instagram_next'),
        url(r'^instagram/?$', 'syte.views.instagram'),
    )

#LastFM Integration
if settings.LASTFM_INTEGRATION_ENABLED:
    urlpatterns += patterns('',
        url(r'^lastfm/(?P<username>\S+)/?$', 'syte.views.lastfm'),
    )

#Statics: Hacky for now... fix this later...
urlpatterns += patterns('',
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url':
        '/static/imgs/favicon.ico'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)




