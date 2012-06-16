
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'willieavendano.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'EyEBauqcTDzML2hRMcP5GHh0MswjyWYiCQLnJP8Ltk9oXUj81P'

#RSS Feed Integration: (by default use Tumblr rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = 'l9wRhv5LWHsgQFfU3wbiGg'
TWITTER_CONSUMER_SECRET = 'eYAea1T0Df1mH4muqMMaPmpFwHqWP8Vp0s3jPllw4o'
TWITTER_USER_KEY = '15119211-LpYHCNVwOpTyjcV9oiVuzXJ6etVcOqZ80Fo6qnxYZ'
TWITTER_USER_SECRET = 'YoBmikCEXRfriI8zUlMfOvF3s0rA55Rini3svg9vOA'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '09b6296ad44fe15af153a0f75b3d31a140383ca8'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '9a8f24256a39d8649ca1'
GITHUB_CLIENT_SECRET = 'a1ab9bae2d7b7aa8b8af1221c0df3f74978cb6c7'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '2616808.826036c.d96fec3f9f1b47d4a09522d2ecd7c117'
INSTAGRAM_USER_ID = '2616808'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = '826036cffcf14a2ab1b91b8b4725f523'
INSTAGRAM_CLIENT_SECRET = '81e426361ddd44cab9e1f891bf32568e'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://quiet-galaxy-5475.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
