var $url;

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
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('#instagram-profile').remove();
         $('#lastfm-profile').remove();
         $('.modal-backdrop').remove();
         $('#soundcloud-profile').remove();
         adjustSelection('home-link');
      }
      else if(this.id == 'instagram-link' && instagram_integration_enabled) {
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('#lastfm-profile').remove();
         $('.modal-backdrop').remove();
         $('#soundcloud-profile').remove();
         adjustSelection('instagram-link');

         setupInstagram(this);
      }
      else if (twitter_integration_enabled && (url.attr('host') == 'twitter.com' || url.attr('host') == 'www.twitter.com')) {

         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#instagram-profile').remove();
         $('#lastfm-profile').remove();
         $('.modal-backdrop').remove();
         $('#soundcloud-profile').remove();
         adjustSelection('twitter-link');

         setupTwitter(url, this);
      }
      else if (github_integration_enabled && (url.attr('host') == 'github.com' || url.attr('host') == 'www.github.com')) {

        $('#twitter-profile').remove();
        $('#dribbble-profile').remove();
        $('#instagram-profile').remove();
        $('#lastfm-profile').remove();
        $('.modal-backdrop').remove();
        $('#soundcloud-profile').remove();
        adjustSelection('github-link');

        setupGithub(url, this);
      }
      else if (dribbble_integration_enabled && (url.attr('host') == 'dribbble.com' || url.attr('host') == 'www.dribbble.com')) {

         $('#twitter-profile').remove();
         $('#github-profile').remove();
         $('#instagram-profile').remove();
         $('#lastfm-profile').remove();
         $('.modal-backdrop').remove();
         $('#soundcloud-profile').remove();
         adjustSelection('dribbble-link');

         setupDribbble(url, this);
      }
      else if (lastfm_integration_enabled && (url.attr('host') == 'lastfm.com' || url.attr('host') == 'www.lastfm.com')) {

        $('#twitter-profile').remove();
        $('#github-profile').remove();
        $('#dribbble-profile').remove();
        $('#instagram-profile').remove();
        $('.modal-backdrop').remove();
        $('#soundcloud-profile').remove();
        adjustSelection('lastfm-link');

        setupLastfm(url, this);
      }
      else if (soundcloud_integration_enabled && (url.attr('host') == 'soundcloud.com' || url.attr('host') == 'www.soundcloud.com')) {

        $('#twitter-profile').remove();
        $('#github-profile').remove();
        $('#dribbble-profile').remove();
        $('#instagram-profile').remove();
        $('.modal-backdrop').remove();
        $('#lastfm-profile').remove();
        adjustSelection('soundcloud-link');

        setupSoundcloud(url, this);
      }
      else {
         window.location = this.href;
      }
  });
}

function adjustSelection(el) {
  $('.main-nav').children('li').removeClass('sel');
  $('#' + el).parent().addClass('sel');

  if (el == 'home-link')
    $url = null;
}

