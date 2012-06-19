
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.3'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'arnonate.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '7ryUGaXxBgV9ExwZQKQJsBlRBwULxTCpF9kerjDyYNzAGcx1PF'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&count=50&screen_name='
TWITTER_CONSUMER_KEY = '0pVFwIWpBbaQDbEZCA'
TWITTER_CONSUMER_SECRET = 'EaxjUhchQCNELhuLKaGqgSiyTT2RK1oBzvWTOcYmb8'
TWITTER_USER_KEY = '18860684-iwm5DBsY4vd6HmhNCQseXoOdgsfw1jNejczwAp68L'
TWITTER_USER_SECRET = 'YyQXWzf5o0IkaYsON79MAwKVktZBPnUwfPQzX7RHw'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '141db2a251680bc72aad6e1da2f445a14d253732'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '890511eff943f6edf199'
GITHUB_CLIENT_SECRET = '1d33a325140a225c3f1b5c5f5cca26d3a0c1c6a8'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '1890903.e79cb5c.9b2190252b4c4f39a1d2b9634d840a65'
INSTAGRAM_USER_ID = '1890903'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = 'e79cb5cafeba4cdbb1b216b67b5ac72c'
INSTAGRAM_CLIENT_SECRET = '2b657b705ec245a2aea18d30806abf4e'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-28905768-1'


if DEPLOYMENT_MODE == 'prod':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://natearnold.me/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
