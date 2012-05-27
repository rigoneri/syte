# Syte

Syte is a easy to setup and deploy personal site that has social integrations like tumblr, twitter, github and dribbble. You can start off by seeing an example of it on my personal website <http://rigoneri.com>

### There is only one rule

You can use, reproduce and do whatever you want with syte as long as you choose a different adjacent color as the ones used by the people below:

[![rigoneri](https://github.com/rigoneri/syte/blob/master/readme-imgs/rigoneri.png?raw=true)](http://rigoneri.com)

Once you have chosen your color and deployed your syte based site, please send a pull request with an image containing the color on the border like the ones above.

## Social Integrations


### Blog: Tumblr

Syte uses [tumblr](http://tumblr.com) for blogging and your blog will be the primary page of the site.

![Syte Home](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-1.png?raw=true)

### Twitter

Syte has twitter integration, which means that every time someone clicks on a link that points to a user's twitter profile the profile is loaded within your site along with the user's latest tweets.

![Syte Twitter](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-2.png?raw=true)

### Github

Syte has github integration, which means that every time someone clicks on a link that points to a user's github profile the profile is loaded within your site along with the user's repos.

![Syte Github](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-3.png?raw=true)

### Dribbble

Syte has dribbble integration, which means that every time someone clicks on a link that points to a user's dribbble profile the profile is loaded within your site along with the user's latest shots.

![Syte Dribbble](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-4.png?raw=true)


## Responsive UI

Syte is also responsive, which means that it scales down to a mobile device screen size.

![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-1.png?raw=true) ![Syte Responsive 1](https://github.com/rigoneri/syte/blob/master/readme-imgs/f-r-2.png?raw=true)

## Technologies Used

Syte uses the [Django](https://www.djangoproject.com/) web framework to handle the requests and call the integration apis (with [python](http://www.python.org/)). However it doesn't necessary needs to be in Django since the majority of the work is on the frontend (I would love to see a fork using [Node.js](http://nodejs.org/), maybe I'll put one together sometime.)

On the frontend Syte uses HTML5 and CSS3 while using the [LESS](http://lesscss.org) css preprocessor. Syte also uses several JS libraries listed below:

* [require.js](http://github.com/jrburke/requirejs)
* [handlebars.js](http://handlebarsjs.com/)
* [moment.js](http://momentjs.com/)
* [spin.js](fgnass.github.com/spin.js)
* [bootstrap-modal.js](http://twitter.github.com/bootstrap/javascript.html#modals)
* [JQuery URL Parser](https://github.com/allmarkedup/jQuery-URL-Parser)

For static compression and minification Syte uses some [Node.js](http://nodejs.org/) libraries:

* [less](http://search.npmjs.org/#/less)
* [uglify-js](http://search.npmjs.org/#/uglify-js) 

For Deployment Syte uses [Heroku](http://www.heroku.com/) since its free for 750 dyno-hours per month. However it doesn't necessary needs to be deployed to Heroku, but the instructions provided are to be deployed there.


## Setup Instructions

[TODO] I'll put these instructions tomorrow...


## Deploy Instructions

[TODO] I'll put these instructions tomorrow...