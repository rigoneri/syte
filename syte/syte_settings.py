
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = '[ENTER TUMBLR BLOG URL] ex. rigoneri.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '[ENTER TUMBLR API KEY HERE, SEE TUMBLR SETUP INSTRUCTIONS]'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&count=50&screen_name='
TWITTER_CONSUMER_KEY = '[ENTER TWITTER CONSUMER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_CONSUMER_SECRET = '[ENTER TWITTER CONSUMER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_KEY = '[ENTER TWITTER USER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_SECRET = '[ENTER TWITTER USER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '[ENTER GITHUB ACCESS TOKEN HERE, SEE GITHUB SETUP INSTRUCTIONS]'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '[ENTER GITHUB CLIENT ID HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_CLIENT_SECRET = '[ENTER GITHUB CLIENT SECRET HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '[ENTER INSTAGRAM ACCESS TOKEN HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_USER_ID = '[ENTER INSTAGRAM USER_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = '[ENTER INSTAGRAM CLIENT_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_CLIENT_SECRET = '[ENTER INSTAGRAM CLIENT_SECRET HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''



if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = '[ENTER PROD URL HERE] ex. http://rigoneri.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
STATIC_URL = SITE_ROOT_URI + 'static/' #specify url for static files
