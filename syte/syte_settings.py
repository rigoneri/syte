
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'blog.sambao21.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '94lu6ky9DAQJQrmQosk3LjgbVYP2QlhpbFkONSjSRGFicA4eeo'


#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = 'Cb3rVarZAMuuujCIc9hZrA'
TWITTER_CONSUMER_SECRET = 'gbh5tVZ0gDUu5t1OESnA3QG0xa25ZuGlS6zS2jfAPKs'
TWITTER_USER_KEY = '34318835-2zZ1i2ejBmSi1kJWbwqT7CvQQYj2KL98g2mpWDsU9'
TWITTER_USER_SECRET = '2hcM9e2sgU7aqcLCzTEQGpGVGmw4rou8FrseN1DLO2U'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_USER_API_URL = 'https://github.com/api/v2/json/user/show/'
GITHUB_REPOS_API_URL = 'https://github.com/api/v2/json/repos/show/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://quiet-wind-9156.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
