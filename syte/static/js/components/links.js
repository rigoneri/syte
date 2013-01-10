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
         adjustSelection('apps');

         var spinner = new Spinner(spin_opts).spin();
         $('#apps-link').append(spinner.el);

         require(["text!templates/apps-view.html"],
            function(apps_view) {
              $(apps_view).modal().on('hidden', function () {
                $(this).remove();
                adjustSelection('home');
              })
              spinner.stop();
            });
      }
      else if(this.id == 'instagram-link' && instagram_integration_enabled) {
         adjustSelection('instagram');
         setupInstagram(this);
      }
      else if (twitter_integration_enabled && (url.attr('host') == 'twitter.com' || url.attr('host') == 'www.twitter.com')) {
         adjustSelection('twitter');
         setupTwitter(url, this);
      }
      else if (github_integration_enabled && (url.attr('host') == 'github.com' || url.attr('host') == 'www.github.com')) {
        adjustSelection('github');
        setupGithub(url, this);
      }
      else if (dribbble_integration_enabled && (url.attr('host') == 'dribbble.com' || url.attr('host') == 'www.dribbble.com')) {
         adjustSelection('dribbble');
         setupDribbble(url, this);
      }
      else if (lastfm_integration_enabled && (url.attr('host') == 'lastfm.com' || url.attr('host') == 'www.lastfm.com')) {
        adjustSelection('lastfm');
        setupLastfm(url, this);
      }
      else if (soundcloud_integration_enabled && (url.attr('host') == 'soundcloud.com' || url.attr('host') == 'www.soundcloud.com')) {
        adjustSelection('soundcloud');
        setupSoundcloud(url, this);
      }
      else if (bitbucket_integration_enabled && (url.attr('host') == 'bitbucket.org' || url.attr('host') == 'www.bitbucket.org')) {
        adjustSelection('bitbucket');
        setupBitbucket(url, this);
      }
      else if(this.id == 'foursquare-link' && foursquare_integration_enabled) {
         adjustSelection('foursquare');
         setupFoursquare(this);
      }
      else if(this.id == 'tent-link' && tent_integration_enabled) {
         adjustSelection('tent');
         setupTent(this);
      }
      else if (this.id == 'steam-link' && steam_integration_enabled) {
        adjustSelection('steam');
        setupSteam(url, this);
      }
      else if (this.id == 'stackoverflow-link' && stackoverflow_integration_enabled) {
         adjustSelection('stackoverflow');
         setupStackoverflow(url, this);
      }
      else {
         window.location = this.href;
      }
  });
}

function adjustSelection(component) {
  $('.modal-backdrop').remove();

  for (c in allComponents) {
    if (allComponents[c] != component) {
      $('#' + allComponents[c] + '-profile').remove();
    }
  }

  if (component != 'apps')
    $('#apps-modal').remove();

  $('.main-nav').children('li').removeClass('sel');
  $('#' + component + '-link').parent().addClass('sel');

  if (component == 'home')
    $url = null;
}

