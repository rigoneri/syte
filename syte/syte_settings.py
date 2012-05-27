
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'rigoneri.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'SnUO903Ld83JE3GD3WE7EBjQzM0ONQ5ludXhE9KZS8JPzyDmlq'


#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = 'ut2m3U9kMiNWazfphjd0jA'
TWITTER_CONSUMER_SECRET = 'JjwTFhChQJdQYujDVgCImCdelBNcacA03VSzUGvHfE'
TWITTER_USER_KEY = '22195551-1QJWj2aARFhTH7iOf49Zq3eEySXus3NqCoF6Iwqw'
TWITTER_USER_SECRET = 'DDcYidylEcihpLDil1yONhMNvUqB84EvwrPEzAdjD0'


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
    SITE_ROOT_URI = 'http://rigoneri.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
