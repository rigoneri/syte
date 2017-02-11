
### :warning: Unmaintained

Sorry, but this project is no longer maintained. Please use the new version, called [Syte2](https://github.com/rigoneri/Syte2).

PS. The project as of June 2016 still works fine if you want to use it.

---

# Syte

Syte is a really simple but powerful packaged personal site that has social integrations like Twitter, GitHub, Dribbble, Instagram, Foursquare, Tumblr, Wordpress, Linkedin, Spotify/Last.fm, SoundCloud, Bitbucket, StackOverflow, Flickr and Steam. You can see it in action on [my personal site](http://rigoneri.herokuapp.com).

## Social Integrations

### Blog

Syte uses [Tumblr](http://tumblr.com) or [Wordpress.com](http://wordpress.com/) for blogging and your blog will be the primary page of the site.

![Syte Home](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-1.png?raw=true)

### Twitter

Syte has Twitter integration, which means that when someone clicks on a link that points to a user's Twitter profile the profile is loaded within your site along with the user's latest tweets.

![Syte Twitter](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-2.png?raw=true)

### GitHub

Syte has GitHub integration, which means that when someone clicks on a link that points to a user's GitHub profile the profile is loaded within your site along with a list of the user's repos.

![Syte GitHub](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-3.png?raw=true)

### Dribbble

Syte has Dribbble integration, which means that when someone clicks on a link that points to a user's Dribbble profile the profile is loaded within your site along with the user's latest shots.

![Syte Dribbble](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-4.png?raw=true)


### Instagram

Syte has Instagram integration, which means that you can show your Instagram pictures within your site like a profile.

![Syte Instagram](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-5.png?raw=true)


### Foursquare

Syte has foursquare integration, which means that you can show your foursquare check-ins within your site like a profile.

![Syte Foursquare](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-9.png?raw=true)


### Last.fm

Syte has Last.fm integration, which means that when someone clicks on a link that points to a user's Last.fm profile the profile information will be loaded directly in the site along with a listing of the most recently scrobbled tracks.

![Syte Lastfm](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-6.png?raw=true)


### SoundCloud

Syte has SoundCloud integration, which means that when someone clicks on a link that points to a user's SoundCloud profile the profile information will be loaded directly in the site along with a listing of the user's SoundCloud tracks. Since I don't use SoundCloud, you can see an example on [Guram's website](http://blog.guramkajaia.com/)

![Syte Soundcloud](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-7.png?raw=true)


### Bitbucket

Syte has Bitbucket integration, which means that when someone clicks on a link that points to a user's Bitbucket profile the profile is loaded within your site along with a list of the user's repos.

![Syte Bitbucket](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-8.png?raw=true)

### Tent.io

Syte has Tent.io integration, which means that you can show your Tent.io public posts within your site like a profile.

![Syte Tent.io](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-10.png?raw=true)

### Steam

Syte has Steam integration, which means that you can show your Steam Community profile within your site.

![Syte Steam](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-11.png?raw=true)

### StackOverflow

Syte has StackOverflow integration, which means that you can show your StackOverflow profile within your site.

![Syte Steam](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-12.png?raw=true)

### Flickr

Syte has Flickr integration, which means that you can show your Flickr photos within your site.

![Syte Flickr](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-13.png?raw=true)

### LinkedIn
Syte has LinkedIn integration, which means that you can show your LinkedIn profile information within your site.

![Syte LinkedIn](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-14.png?raw=true)

## Responsive UI

Syte is responsive, which means that it scales down to a mobile device screen size.

![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-1.png?raw=true) ![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-2.png?raw=true)

## Technologies Used

Syte uses the [Django](https://www.djangoproject.com/) web framework to handle requests and call the integration APIs (with [python](http://www.python.org/)). However it doesn't necessarily need to be in Django since the majority of the work is on the frontend (I would love to see a fork using [Node.js](http://nodejs.org/), maybe I'll put one together sometime.)

On the frontend Syte uses HTML5 and CSS3 while using the [LESS](http://lesscss.org) CSS preprocessor. Syte also uses several JS libraries listed below:

* [require.js](http://github.com/jrburke/requirejs)
* [handlebars.js](http://handlebarsjs.com/)
* [moment.js](http://momentjs.com/)
* [spin.js](fgnass.github.com/spin.js)
* [bootstrap-modal.js](http://twitter.github.com/bootstrap/javascript.html#modals)
* [jQuery URL Parser](https://github.com/allmarkedup/jQuery-URL-Parser)
* [google-code-prettify](http://google-code-prettify.googlecode.com/svn/trunk/README.html)

For static compression and minification Syte uses some [Node.js](http://nodejs.org/) libraries:

* [less](http://search.npmjs.org/#/less)
* [uglify-js](http://search.npmjs.org/#/uglify-js)

For deployment Syte uses [Heroku](http://www.heroku.com/) since it's free for 750 dyno-hours per month. While the included instructions are for Heroku, Syte doesn't necessarily need to be deployed there.


## Setup Instructions

There are a few steps in order to get Syte configured, but don't worry they are pretty easy.

`Note` I recommend you branching your fork and not checking in sensitive settings to GitHub!
`Warning` Do not place OAuth keys and tokens in a public repository.

### Base content changes

There are a few things that are defaulted to have my information so you have the initial structure of the site.

To start off change the **pictures** to have your picture, navigate to `syte > static > imgs` and replace **pic.png** with your picture and **favicon.ico** with your favicon in this case I use my picture as well. Please make sure you keep the same sizes. **pic.png** is 84x84px and **favicon.ico** is 32x32px.

Then make some text and link changes. Open **base.html** located in `syte > templates > base.html` and make the following changes:

1. Change the `meta="description"` content to have a description about you.
2. Change the `meta="keywords"` content to have keywords about you.
3. Change the `title` tag to have your name.
4. Inside the `header` tag change the `h1` tag to have your name.
5. Inside the `header` tag change the `h2` tag to have a short description about you.
6. Inside the `nav` tag change the **twitter-link** href to point to your twitter profile, if you don't have twitter just remove that whole line.
7. Inside the `nav` tag change the **github-link** href to point to your GitHub profile, if you don't have GitHub just remove that whole line.
8. Inside the `nav` tag change the **dribbble-link** href to point to your Dribbble profile, if you don't have Dribbble just remove that whole line.
9. Inside the `nav` tag change the **steam-link** href to point to your Steam community profile, if you don't have Steam just remove that whole line.
10. Inside the `nav` tag change the **stackoverflow-link** href to point to your StackOverflow profile, if you don't have StackOverflow just remove that whole line.
11. Inside the `nav` tag change the **flickr-link** href to point to your Flickr profile, if you don't have Flickr just remove that whole line.
12. Inside the `nav` tag change the **contact-link** href to point to your email address.
13. Under `class="mobile-nav"` div change the **h3** link text to have your domain name or your name.

Then pick your **adjacent color** and change the `@adjacent-color` hex value in variables.less located in `syte > static > less > variables.less` Make sure the color you chose is not used by anyone on the list up above. If you want blue pick a different shade of blue, there are hundreds out there...




### Setting up your blog

Syte uses Tumblr or Wordpress for blogging.

#### Setting up Tumblr

If you have a Tumblr blog you will need to get the `api_key` needed to call their APIs. In order to do that **register your site** with them by going to <http://www.tumblr.com/oauth/register>, fill in the information about your site, there is no need to enter a default callback url or an icon. Once you are done your website will be listed under <http://www.tumblr.com/oauth/apps>, save the `OAuth Consumer Key` value that's the `api_key` we need for Syte.

Once you have the `api_key` from Tumblr you have to enter it in **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the key under `TUMBLR_API_KEY`, also please enter your Tumblr url under `TUMBLR_BLOG_URL` see the example on how it should be formatted.

#### Setting up Wordpress

For now Syte only support wordpress blogs that are build using [wordpress.com](http://wordpress.com).

Open `syte > syte_settings.py` and under `WORDPRESS_BLOG_URL` enter ther url of your wordpress.com blog, also under `BLOG_PLATFORM` set it to "wordpress".

#### Comments

Comments are available through [Disqus](http://disqus.com/) in order to get yours setup, make sure to signup through their website. Once you are done you will be given a Disqus shortname. Grab the shortname and enter it in **syte_settings.py** under `DISQUS_SHORTNAME`, also make sure to have `DISQUS_INTEGRATION_ENABLED` set to True in order to work.





### Setting up Twitter integration

Twitter has another level of security, therefore we need more information instead of just an api_key like Tumblr. To get started create a new application on Twitter for your website by going to <https://dev.twitter.com/apps/new>. Once you are done creating your application you will be taken to your application page on Twitter, there you already have two pieces of the puzzle, the `Consumer key` and the `Consumer secret` make sure you save those.

Next you will need your access tokens, on the bottom of that page there is a link called **Create my access token** click on that. Once you are done you will be given the other two pieces of the puzzle, the `Access token` and the `Access token secret` make sure you save those as well.

Once you have those four items from Twitter you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* `Consumer key` string you saved under `TWITTER_CONSUMER_KEY`
* `Consumer secret` string you saved under  `TWITTER_CONSUMER_SECRET`
* `Access token` string you saved under `TWITTER_USER_KEY`
* `Access token secret` string you saved under `TWITTER_USER_SECRET`

If you want to turn off the Twitter integration just set `TWITTER_INTEGRATION_ENABLED` to False.




### Setting up GitHub integration

GitHub has the same level of security as Twitter, but they don't provide a button that makes it easy to get the access token, so instead we have to get the access token ourselves. To get started sign in to GitHub and go to <https://github.com/settings/applications/new> to register your application.

Enter the ***Application Name***, ***Main URL*** and ***Callback URL***. For the Callback URL enter `http://127.0.0.1:8000/github/auth` for now since we will get the access token while running it locally. Once you are done registering your application you will be given the ***Client ID*** and ***Client Secret***.

Once you have those two items from GitHub you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Client ID*** under `GITHUB_CLIENT_ID`
* ***Client Secret*** under `GITHUB_CLIENT_SECRET`

After you have entered those two items, follow the steps below for running your Syte locally on your machine. Once you have your Syte running navigate to `http://127.0.0.1:8000/github/auth`, you will be taken to GitHub's website and will be asked to sign in and authorize your application. After you authorized your application you will be taken back to your Syte and you will be given your ***Access Token***

You can also get your access token via the GitHub api using curl:
```
curl -i -u "username:password" https://api.github.com/authorizations
```

Once you have your access token from GitHub you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter it under `GITHUB_ACCESS_TOKEN`

After you validated that your GitHub integration worked go back to GitHub page and change the ***Callback URL*** field to have your domain info (this is not required), then make sure you turn off the GitHub OAuth integration setting so you don't make that available to everyone in the Internet. You can do that by setting `GITHUB_OAUTH_ENABLED` to False.

If you want to turn off GitHub integration just set `GITHUB_INTEGRATION_ENABLED` to False.




### Setting up Dribbble integration

To get started go to <http://developer.dribbble.com/> and click on **Register a New Application**.

Enter ***Name***, ***Description***, ***Website URL*** and ***Callback URL***. After that is done Dribbble will give you a **Client Access Token** to use.

Once you have your access token from Dribbble you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter it under `DRIBBBLE_ACCESS_TOKEN`

If you want to turn off this feature just set `DRIBBBLE_INTEGRATION_ENABLED` setting to False in syte_settings.py.


### Setting up Instagram integration

Instagram has the same level of security as GitHub and similar steps on getting the access token ourselves. To get started go to <http://instagram.com/developer/>, sign in and crate a new client by clicking on the ***Manage Clients*** link on the top right side.

Enter the ***Application Name***, ***Description***, ***Website*** and ***OAuth redirect_Uri***. For the OAuth redirect_uri enter `http://127.0.0.1:8000/instagram/auth/` for now since we will get the access token while running it locally. The trailing slash is required for Instagram not to complain that the redirect_Uri is wrong. Once you are done registering your client you will be given the ***Client ID*** and ***Client Secret***.

Once you have those two items from Instagram you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Client ID*** under `INSTAGRAM_CLIENT_ID`
* ***Client Secret*** under `INSTAGRAM_CLIENT_SECRET`

After you have entered those two items, follow the steps below for running your Syte locally on your machine. Once you have your Syte running navigate to `http://127.0.0.1:8000/instagram/auth`, you will be taken to Instagram's website and will be asked to sign in and authorize your application. After you authorized your application you will be taken back to your Syte and you will be given your ***Access Token*** and your ***User ID***

Once you have those two items from Instagram you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Access Token*** under `INSTAGRAM_ACCESS_TOKEN`
* ***User ID*** under `INSTAGRAM_USER_ID`

After you validated that your Instagram integration worked go back to Instagram page and change the ***OAuth redirect_uri*** field to have your domain info (this is not required), then make sure you turn off the Instagram OAuth integration setting so you don't make that available to everyone in the Internet. You can do that by setting `INSTAGRAM_OAUTH_ENABLED` to False.

If you want to turn off Instagram integration just set `INSTAGRAM_INTEGRATION_ENABLED` to False.


### Setting up Foursquare integration

Foursquare has the same level of security as Instagram and similar steps on getting the access token ourselves. To get started go to <https://foursquare.com/oauth>, sign in and register a new consumer.

Enter the ***Application Name***, ***Application Website*** and ***Callback URL***. For the callback url enter `http://127.0.0.1:8000/foursquare/auth` for now since we will get the access token while running it locally. Once you are done registering your consumer you will be given the ***Client ID*** and ***Client Secret***.

Once you have those two items from Foursquare you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Client ID*** under `FOURSQUARE_CLIENT_ID`
* ***Client Secret*** under `FOURSQUARE_CLIENT_SECRET`

After you have entered those two items, follow the steps below for running your Syte locally on your machine. Once you have your Syte running navigate to `http://127.0.0.1:8000/foursquare/auth`, you will be taken to Foursquare's website and will be asked to sign in and authorize your application. After you authorized your application you will be taken back to your Syte and you will be given your ***Access Token***.

Once you have the access token from Foursquare you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Access Token*** under `FOURSQUARE_ACCESS_TOKEN`

After you validated that your foursquare integration worked go back to Foursquare page and change the ***Callback URL*** field to have your domain info (this is not required), then make sure you turn off the foursquare OAuth integration setting so you don't make that available to everyone in the Internet. You can do that by setting `FOURSQUARE_OAUTH_ENABLED` to False.

If you want to turn off Instagram integration just set `FOURSQUARE_INTEGRATION_ENABLED` to False.

Additionally if you don't want people to know where you are currently at, you can set 'FOURSQUARE_SHOW_CURRENT_DAY' to False and it will only show check-ins more than a day old.



### Setting up Last.fm integration

The Last.fm integration does not make any authenticated calls so setting it up only requires that you register an application with Last.fm and get an API key.

To get an API key simply follow the [Getting started instructions](http://www.last.fm/api).  You can then view your API Key from [your api account page](http://www.last.fm/api/account).

Once you have your API Key from Last.fm you have to enter it in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***API_KEY*** under `LASTFM_API_KEY`
* ***USERNAME*** under `LASTFM_USERNAME`

If you want to turn off Last.fm integration just set `LASTFM_INTEGRATION_ENABLED` to False.


### Setting up SoundCloud integration

In order to setup the SoundCloud integration you first need to create a SoundCloud application by going to <http://soundcloud.com/you/apps>. Once you have the `CLIENT_ID` from SoundCloud open the **syte_settings.py** file and enter it under the `SOUNDCLOUD_CLIENT_ID` setting.

Inside **syte_settings.py** there are two other options to configure how your SoundCloud tracks will be shown.

* `SOUNDCLOUD_SHOW_ARTWORK` (Boolean) set this option to true if you want to show your track artwork on page.
* `SOUNDCLOUD_PLAYER_COLOR` you can set your widget theme color here. Use Hex values only without `#`

If you want to turn off SoundCloud integration just set `SOUNDCLOUD_INTEGRATION_ENABLED` to False.


### Setting up Bitbucket integration

The Bitbucket integration does not make any authenticated calls nor does it require a registered API key.

If you want to turn off Bitbucket integration just set `BITBUCKET_INTEGRATION_ENABLED` to False.

#### Comment
To display the fork count on repositories set `BITBUCKET_SHOW_FORKS` to True.  The Bitbucket API require one call for each repository to get fork count, which is disabled by default.

The Bitbucket API throttles the user resource to 100 calls every 30 minutes.


### Setting up Tent.io integration

The Tent.io integration does not make any authenticated calls nor does it require a registered API key.

If you want to turn off Tent.io integration just set `TENT_INTEGRATION_ENABLED` to False.

Inside **syte_settings.py** there are two other options to configure your Tent.io entity.

* ***Your Entity-URI*** under `TENT_ENTITY_URI`
* ***URL to a Feed or Tent-Status*** under `TENT_FEED_URL`

### Setting up Steam integration

In order to setup Steam integration you first need to create a Steam Web API key by going to <http://steamcommunity.com/dev/apikey>. Once you have the `STEAM WEB API KEY` from Steam open the **syte_settings.py** file and enter it under the `STEAM_API_KEY` setting.

If you want to turn off Steam integration just set `STEAM_INTEGRATION_ENABLED` to False.

### Setting up StackOverflow integration

The StackOverflow integration does not make any authenticated calls nor does it require a registered API key.

If you want to turn off StackOverflow integration just set `STACKOVERFLOW_INTEGRATION_ENABLED` to False.

### Setting up Flickr integration

The Flickr integration does not make any authenticated calls nor does it require a registered API key.

To make it work, you'll need to find your Flickr ID. This is different to your username, and you can do the lookup here: <http://idgettr.com/>

If you want to turn off Flickr integration just set `FLICKR_INTEGRATION_ENABLED` to False.

### Setting up LinkedIn integration

LinkedIn has the same level of security as Instagram and Foursquare and similar steps on getting the access token ourselves. To get started create a new application on LinkedIn for your website by going to <https://developer.linkedin.com/>. Once you are done creating your application you will be taken to your application page on LinkedIn, there you already have a few pieces of the puzzle, the `Api Key`, `Secret Key`, make sure you save those.

In that same page make sure to enter `http://127.0.0.1:8000/linkedin/auth/` under Oauth 2.0 Redirect URls.

Once you have those items from LinkedIn you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* `Consumer key` string you saved under `LINKEDIN_API_KEY`
* `Consumer secret` string you saved under  `LINKEDIN_API_SECRET`

After you have entered those two items, follow the steps below for running your Syte locally on your machine. Once you have your Syte running navigate to `http://127.0.0.1:8000/linkedin/auth`, you will be taken to Linkedin's website and will be asked to sign in and authorize your application. After you authorized your application you will be taken back to your Syte and you will be given your ***Access Token***.

Once you have the access token from Foursquare you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* ***Access Token*** under `LINKEDIN_TOKEN`

If you want to turn off the LinkedIn integration just set `LINKEDIN_INTEGRATION_ENABLED` to False.


## Running & Deployment Instructions

Now that you have everything setup and ready to go we will be able to run the project locally and deploy to Heroku or AWS with the instructions below. Please note that these instructions are for Mac, which should be the same for Linux systems. If you have problems with these instructions on Windows, let me know or send a pull request.



### Running Syte locally

Running locally is really easy if you are on a Mac since you already have some stuff installed out of the box. To start off install these python packages:

* [virtualenv](http://www.virtualenv.org/en/latest/index.html)
* [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)

Once you have those two installed go to your Syte directory and run the following commands:

```
$ mkvirtualenv syte
$ workon syte
(syte)$ pip install --use-mirrors -r requirements.txt
```

`Note` On Mac/Linux you need to modify your shell startup file to add mkvirtualenv and workon commands, see [virtualenvwrapper installation instructions](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file)

This will install all the project dependencies listed in requirements.txt including Django. Now all you have to do is run the Django project and go to <http://127.0.0.1:8000>.

```
python manage.py runserver
```

### Compressing Statics

Compressing static files like CSS and JS are done using [Node.js](http://nodejs.org/). This step is important since it will get all your static files and make tiny bit small so your site can be run faster when it's out there on the so called World Wide Web :)

In order to get there you need to first install [node.js](http://nodejs.org/), they have automatic installers which makes installation really easy. Then you need to install [Node Package Manager (npm)](http://npmjs.org/) by running the following command:

```
curl http://npmjs.org/install.sh | sudo sh
```

After npm is installed you need to install two node packages `less` and `uglify-js`. To do that run the following commands:

```
sudo npm install less -g
sudo npm install uglify-js -g
```

`Note` windows users be sure to create the directories `syte > static > css` and `syte > static > js > min` first if it doesn't already exist.

Then whenever you want to release a new version of static update the `COMPRESS_REVISION_NUMBER` in **syte-settings.py** and run the compress python command from your syte directory:

```
python compress.py
```

This will create a minified version of your CSS in `syte > static > css` and the minified version of your JavaScript in `syte > static > js > min`.

`Note` If you are using Windows and is having problems on compressing statics checkout issue [#14](https://github.com/rigoneri/syte/issues/14) to see if it helps.


### Deploying to Heroku

Deploying to Heroku is extremely easy and free, that's why I chose it over Amazon or similar. That's another fork I would love to see, different deployment instructions maybe to an Amazon EC2 micro instance.

First signup to [Heroku](http://heroku.com) then follow these simple [Django deployment instructions](https://devcenter.heroku.com/articles/django) I already have the requirements.txt and the Procfile ready to go, but before you actually deploy there are two things you need to change:

1. Change the ``DEPLOYMENT_MODE`` value to prod in **syte_settings.py** located in ``syte > syte_settings.py``
2. Change the ``SITE_ROOT_URI`` value to your Heroku app url in **syte_settings.py** see the available example to how it should be formatted.


### Deploying to AWS

Deploying to [AWS](http://aws.amazon.com) is a little more complicated than Heroku, but is a nice alternative.  The easiest way to deploy your application to AWS is by using [AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_django.html).  To help keep costs low, we will deploy to micro instances.

First signup to [AWS](http://aws.amazon.com) then follow the instructions below.  I have already included some of the required files for you (see syte.config in .ebextensions directory).  The other required files will be created automatically, but some of the settings may need to be altered slightly.

1. Change the ``DEPLOYMENT_MODE`` value to prod in **syte_settings.py** located in ``syte > syte_settings.py``
2. Change the ``SITE_ROOT_URI`` value to your AWS app url in **syte_settings.py** see the available example to how it should be formatted.
3. Install the eb command-line tools and add to your path.  Download from [here](http://aws.amazon.com/code/6752709412171743).  This will allow us to control AWS from the command-line.
4. Execute the `eb init` command in the root of the syte repo and follow the on-screen instructions.  This will help get our project ready to be deployed into AWS.  Please note: during this step you will be asked to provide security credentials.  If you are not sure what to use, see [here](http://docs.aws.amazon.com/general/latest/gr/getting-aws-sec-creds.html)
5. Execute the `eb start` command to deploy a sample application to AWS.  Once this command completes execute `eb status --verbose` and confirm that the sample application is running at the provided url.
6. Let's make sure our configurations are right.
   - First, open ./ebextensions/syte.config and confirm the settings here.  You should not have to update anything.
   - Second, open the ./elasticbeanstalk/opensettings.XXX-env (where XXX-env is the name of your environment).  Update this by updating:
     DJANGO_SETTINGS_MODULE=syte.settings
     StaticFiles=syte/static=
     WSGIPath=syte/wsgi.py
7. To make sure the above changes are not reverted, execute `eb update`.
8. Deploy the repo to AWS by executing `git aws.push`.  This command can be rerun whenever you have changes that you want to deploy.
9. Execute `eb status --verbose` or monitor the provisioning process on AWS' website.  To troubleshoot, go to the ElasticBeanstalk section of AWS, get a snapshot of the logs and review them for errors.



## Contributing

There are plans for several services to be added in the
[TODO file](https://github.com/rigoneri/syte/blob/master/TODO.md).  One of
these services is a good place to start when looking for ways to help.  Also
posting/fixing [issues](https://github.com/rigoneri/syte/issues) is always
helpful.

If you would like to add support for a new service you might find the [HELP
file](https://github.com/rigoneri/syte/blob/master/HELP.md) useful on how to
get started and where your new code might go, etc.

Also, the [DESIGN file](https://github.com/rigoneri/syte/blob/master/DESIGN.md)
can be a useful resource when starting out with the project and trying to
understand roughly how it all fits together.




## Credit

Syte was developed by **Rigo** (rodrigo neri). Check his personal site out at <http://rigoneri.com> and follow him on twitter [@rigoneri](http://twitter.com/#!/rigoneri)


## License


The MIT License

Copyright (c) 2012, Rodrigo Neri <@rigoneri>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
