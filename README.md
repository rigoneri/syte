# Syte

Syte is a really simple but powerful packaged personal site that has social integrations like tumblr, twitter, github, dribbble and instagram. You can see it in action on my personal site <http://rigoneri.com>

### There is only one rule

You can use, reproduce and do whatever you want with syte as long as you choose a different adjacent color as the ones used by the people below. Once you have chosen your color and deployed your Syte based site, please send a pull request with an image of you containing the color on the border like the ones above.

[![rigoneri](https://github.com/rigoneri/syte/blob/master/readme-imgs/rigoneri.png?raw=true)](http://rigoneri.com)
[![sambao21](https://github.com/rigoneri/syte/blob/master/readme-imgs/sambao21.png?raw=true)](http://sambao21.com)
[![keithentzeroth](https://github.com/rigoneri/syte/blob/master/readme-imgs/keithentzeroth.png?raw=true)](http://keithentzeroth.com)
[![garrypolley](https://github.com/rigoneri/syte/blob/master/readme-imgs/garrypolley.png?raw=true)](http://garrypolley.com)
[![href(https://github.com/rigoneri/syte/blob/master/readme-imgs/href.png?raw=true)(http://blog.stacktrace.ch)

## Social Integrations


### Blog: Tumblr

Syte uses [tumblr](http://tumblr.com) for blogging and your blog will be the primary page of the site.

![Syte Home](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-1.png?raw=true)

### Twitter

Syte has twitter integration, which means that when someone clicks on a link that points to a user's twitter profile the profile is loaded within your site along with the user's latest tweets.

![Syte Twitter](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-2.png?raw=true)

### Github

Syte has github integration, which means that when someone clicks on a link that points to a user's github profile the profile is loaded within your site along with a list of the user's repos.

![Syte Github](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-3.png?raw=true)

### Dribbble

Syte has dribbble integration, which means that when someone clicks on a link that points to a user's dribbble profile the profile is loaded within your site along with the user's latest shots.

![Syte Dribbble](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-4.png?raw=true)


### Instagram

Syte has instagram integration, which means that you can show your instagram pictures within your site like a profile. Currently the only way to display your pictures is through their iPhone and Android apps, this is not even possible through their website.

![Syte Instagram](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-5.png?raw=true)

## Responsive UI

Syte is responsive, which means that it scales down to a mobile device screen size.

![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-1.png?raw=true) ![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-2.png?raw=true)

## Technologies Used

Syte uses the [Django](https://www.djangoproject.com/) web framework to handle requests and call the integration apis (with [python](http://www.python.org/)). However it doesn't necessarily need to be in Django since the majority of the work is on the frontend (I would love to see a fork using [Node.js](http://nodejs.org/), maybe I'll put one together sometime.)

On the frontend Syte uses HTML5 and CSS3 while using the [LESS](http://lesscss.org) CSS preprocessor. Syte also uses several JS libraries listed below:

* [require.js](http://github.com/jrburke/requirejs)
* [handlebars.js](http://handlebarsjs.com/)
* [moment.js](http://momentjs.com/)
* [spin.js](fgnass.github.com/spin.js)
* [bootstrap-modal.js](http://twitter.github.com/bootstrap/javascript.html#modals)
* [JQuery URL Parser](https://github.com/allmarkedup/jQuery-URL-Parser)
* [google-code-prettify](http://google-code-prettify.googlecode.com/svn/trunk/README.html)

For static compression and minification Syte uses some [Node.js](http://nodejs.org/) libraries:

* [less](http://search.npmjs.org/#/less)
* [uglify-js](http://search.npmjs.org/#/uglify-js) 

For deployment Syte uses [Heroku](http://www.heroku.com/) since it's free for 750 dyno-hours per month. While the included instructions are for Heroku, Syte doesn't necessarily need to be deployed there.
	

## Setup Instructions

There are a few steps in order to get Syte configured, but don't worry they are pretty easy.

`Note` I recommend you branching your fork and not checking in sensitive settings to github!

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
7. Inside the `nav` tag change the **github-link** href to point to your github profile, if you don't have github just remove that whole line.
8. Inside the `nav` tag change the **dribbble-link** href to point to your dribbble profile, if you don't have dribbble just remove that whole line.
9. Inside the `nav` tag change the **contact-link** href to point to your email address. 
10. Under `class="mobile-nav"` div change the **h3** link text to have your domain name or your name.

Then pick your **adjacent color** and change the `@adjacent-color` hex value in variables.less located in `syte > static > less > variables.less` Make sure the color you chose is not used by anyone on the list up above. If you want blue pick a different shade of blue, there are hundreds out there...
  
	
	

### Setting up your blog (Tumblr)

If you already have a tumblr blog good! If you don't [signup for one here](https://www.tumblr.com/) it's really easy! I might eventually make Syte integrate with wordpress as well, if you beat me to it please send a pull request.

Once you have your tumblr blog you will need to get the `api_key` needed to call their APIs. In order to do that **register your site** with them by going to <http://www.tumblr.com/oauth/register>, fill in the information about your site, there is no need to enter a default callback url or an icon. Once you are done your website will be listed under <http://www.tumblr.com/oauth/apps>, save the `OAuth Consumer Key` value that's the `api_key` we need for Syte.

Once you have the `api_key` from tumblr you have to enter it in **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the key under `TUMBLR_API_KEY`, also please enter your tumblr url under `TUMBLR_BLOG_URL` see the example on how it should be formatted.
  
	
	


### Setting up Twitter integration

Twitter has another level of security, therefore we need more information instead of just an api_key like tumblr. To get started create a new application on twitter for your website by going to <https://dev.twitter.com/apps/new>. Once you are done creating your application you will be taken to your application page on twitter, there you arleady have two pieces of the puzzle, the `Consumer key` and the `Consumer secret` make sure you save those.

Next you will need your access tokens, on the bottom of that page there is a link called **Create my access token** click on that. Once you are done you will be given the other two pieces of the puzzle, the `Access token` and the `Access token secret` make sure you save those as well.

Once you have those four items from twitter you have to enter them in your **syte_settings.py** located in `syte > syte_settings.py`. Once you open that file enter the following:

* `Consumer key` string you saved under `TWITTER_CONSUMER_KEY`
* `Consumer secret` string you saved under  `TWITTER_CONSUMER_SECRET`
* `Access token` string you saved under `TWITTER_USER_KEY`
* `Access token secret` string you saved under `TWITTER_USER_SECRET`

If you want to turn off the twitter integration just set `TWITTER_INTEGRATION_ENABLED` to False.
  
	
	

### Setting up Github integration

You don't have to do anything to setup the github integration. If you want to turn off this feature just set `GITHUB_INTEGRATION_ENABLED` setting to False in syte_settings.py.
  
	
	

### Setting up Dribbble integration

You don't have to do anything to setup the dribbble integration. If you want to turn off this feature just set `DRIBBBLE_INTEGRATION_ENABLED` setting to False in syte_settings.py.

   
   
   
### Setting up Instagram integration

Instagram has the same level of security as twitter, but they don't provide a button that makes it easy to get the access token, so instead we have to get the access token ourselves. To get started go to <http://instagram.com/developer/>, sign in and crate a new client by clicking on the ***Manage Clients*** link on the top right side.

Enter the ***Application Name***, ***Description***, ***Website*** and ***OAuth redirect_uri***. For the OAuth redirect_uri enter `http://127.0.0.1:8000/instagram/auth` for now since we will get the access token while running it locally. Once you are done regestering your client you will be given the ***Client ID*** and ***Client Secret***. 

Once you have those two items from Instagram you have to enter them in your **syte_settings.py** located in `syte > syste_settings.py`. Once you open that file enter the following:

* ***Client ID*** under `INSTAGRAM_CLIENT_ID`	
* ***Client Secret*** under `INSTAGRAM_CLIENT_SECRET`
   
After you have entered those two items, folow the steps below for running your Syte locally on your machine. Once you have your Syte running navigate to `http://127.0.0.1:8000/instagram/auth`, you will be taken to Instagram's website and will be asked to sign in and authorize your application. After you authorized your application you will be taken back to your Syte and you will be given your ***Access Token*** and your ***User ID***

Once you have those two items from Instagram you have to enter them in your **syte_settings.py** located in `syte > syste_settings.py`. Once you open that file enter the following:

* ***Access Token*** under `INSTAGRAM_ACCESS_TOKEN`
* ***User ID*** under `INSTAGRAM_USER_ID`

After you validated that your instagram integration worked go back to Instragam page and change the ***OAuth redirect_uri*** field to have your domain info (this is not required), then make sure you turn off the instagram oauth interation setting so you don't make that available to everyone in the internet. You can do that by setting `INSTAGRAM_OAUTH_ENABLED` to False.

If you want to turn off instagram integration just set `INSTAGRAM_INTEGRATION_ENABLED` to False.




## Running & Deployment Instructions

Now that you have everything setup and ready to go we will be able to run the project locally and deploy to heroku with the instructions below. Please note that these instructions are for Mac, which should be the same for linux systems. If you have problems with these instructions on Windows, let me know or send a pull request. 
  
	
	

### Running Syte locally 

Running locally is really easy if you are on a Mac since you already have some stuff installed out of the box. To start off install these python packages:

* [virtualenv](http://www.virtualenv.org/en/latest/index.html)
* [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)

Once you have those two installed go to your syte directory and run the following commands:

```
$ mkvirtualenv syte
$ workon syte
(syte)$ pip install --use-mirrors -r requirements.txt 
```

This will install all the project dependencies listed in requirements.txt including Django. Now all you have to do is run the django project and go to <http://127.0.0.1:8000>.

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

`Note` be sure to create the directories `syte > static > css` and `syte > static > js > min` first if it doesn't already exist.

Then whenever you want to release a new version of static update the `COMPRESS_REVISION_NUMBER` in **syte-settings.py** and run the compress python command from your syte directory:

```
python compress.py
```

This will create a minified version of your CSS in `syte > static > css` and the minified version of your JavaScript in `syte > static > js > min`.


### Deploying to Heroku

Deploying to Heroku is extremely easy and free, that's why I chose it over Amazon or similar. That's another fork I would love to see, different deployment instructions maybe to an Amazon EC2 micro instance.

First signup to [Heroku](http://heroku.com) then follow these simple [Django deployement instructions](https://devcenter.heroku.com/articles/django) I already have the requirements.txt and the Procfile ready to go, but before you actually deploy there are two things you need to change:

1. Change the ``DEPLOYMENT_MODE`` value to prod in **syte_settings.py** located in ``syte > syte_settings.py``
2. Change the ``SITE_ROOT_URI`` value to your heroku app url in **syte_settings.py** see the available example to how it should be formatted.

	
	


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

####There is only one rule####

You choose a different adjacent color as the ones used by the people listed up above. Once you have chosen your color and deployed your Syte based site, please send a pull request with an image of you containing the color on the border.
