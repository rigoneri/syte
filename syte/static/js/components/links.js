var $url;

var allComponents = [
  'instagram',
  'twitter',
  'github',
  'dribbble',
  'lastfm',
  'soundcloud',
  'bitbucket',
  'foursquare',
  'tent',
  'steam',
  'stackoverflow'
];

currSelection = 'home';

function setupLinks() {

  $('a').click(function(e) {
      if (e.which == 2)
          return;
      e.preventDefault();
      e.stopPropagation();

      if (this.href == $url)
          return;

      var url = $.url(this.href.replace('/#!', ''));
      $url = this.href;

      if (this.id == 'home-link' && window.location.pathname == '/') {
        adjustSelection('home');
      }
      else if (this.id == 'apps-link') {
         adjustSelection('apps', function() {
           var spinner = new Spinner(spin_opts).spin();
           $('#apps-link').append(spinner.el);

            require.config({
              urlArgs: "bust=v1" 
            })

           require(["text!templates/apps-view.html"],
              function(apps_view) {
                var template = Handlebars.compile(apps_view);
                $(template()).modal().on('hidden', function () {
                  $(this).remove();
                  if (currSelection === 'apps') {
                    adjustSelection('home');
                  }
                })
                spinner.stop();
              });
        });
      }
      else if(this.id == 'instagram-link' && instagram_integration_enabled) {
        adjustSelection('instagram', setupInstagram.bind(this, this));
      }
      else if (twitter_integration_enabled && (url.attr('host') == 'twitter.com' || url.attr('host') == 'www.twitter.com')) {
        adjustSelection('twitter', setupTwitter.bind(this, url, this));
      }
      else if (github_integration_enabled && (url.attr('host') == 'github.com' || url.attr('host') == 'www.github.com')) {
        adjustSelection('github', setupGithub.bind(this, url, this));
      }
      else if (dribbble_integration_enabled && (url.attr('host') == 'dribbble.com' || url.attr('host') == 'www.dribbble.com')) {
        adjustSelection('dribbble', setupDribbble.bind(this, url, this));
      }
      else if (lastfm_integration_enabled && (url.attr('host') == 'lastfm.com' || url.attr('host') == 'www.lastfm.com')) {
        adjustSelection('lastfm', setupLastfm.bind(this, url, this));
      }
      else if (soundcloud_integration_enabled && (url.attr('host') == 'soundcloud.com' || url.attr('host') == 'www.soundcloud.com')) {
        adjustSelection('soundcloud', setupSoundcloud.bind(this, url, this));
      }
      else if (bitbucket_integration_enabled && (url.attr('host') == 'bitbucket.org' || url.attr('host') == 'www.bitbucket.org')) {
        adjustSelection('bitbucket', setupBitbucket.bind(this, url, this));
      }
      else if(this.id == 'foursquare-link' && foursquare_integration_enabled) {
        adjustSelection('foursquare', setupFoursquare.bind(this, this));
      }
      else if(this.id == 'tent-link' && tent_integration_enabled) {
        adjustSelection('tent', setupTent.bind(this, this));
      }
      else if (this.id == 'steam-link' && steam_integration_enabled) {
        adjustSelection('steam', setupSteam.bind(this, url, this));
      }
      else if (this.id == 'stackoverflow-link' && stackoverflow_integration_enabled) {
        adjustSelection('stackoverflow', setupStackoverflow.bind(this, url, this));
      }
      else {
        window.location = this.href;
      }
  });
}

function adjustSelection(component, callback) {
  var transition,
      $currProfileEl;

  if (currSelection !== 'home') {
    $currProfileEl = $('#' + currSelection + '-profile');
    if (currSelection === 'apps') {
      $currProfileEl = $('#apps-modal');
    }
    transition = $.support.transition && $currProfileEl.hasClass('fade'),
    $currProfileEl.modal('hide');
    if (callback) {
      if (transition) {
        $currProfileEl.one($.support.transition.end, callback);
      }
      else {
        callback();
      }
    }
  }
  else if (callback) {
    callback();
  }
/*
  if (component != 'apps')
    $('#apps-modal').remove();
*/
  $('.main-nav').children('li').removeClass('sel');
  $('#' + component + '-link').parent().addClass('sel');

  if (component == 'home')
    $url = null;

  currSelection = component;
}

