
function setupLinks() {

  $('a').click(function(e) {
      e.preventDefault();
      e.stopPropagation();

      var url = $.url(this.href.replace('/#!', ''));

      if (this.id == 'home-link' && window.location.pathname == '/') {
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('#instagram-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('home-link');
      }
      else if(this.id == 'instagram-link' && instagram_integration_enabled) {
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('instagram-link');

         setupInstagram(this);
      }
      else if (twitter_integration_enabled && (url.attr('host') == 'twitter.com' || url.attr('host') == 'www.twitter.com')) {

         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#instagram-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('twitter-link');

         setupTwitter(url, this);
      }
      else if (github_integration_enabled && (url.attr('host') == 'github.com' || url.attr('host') == 'www.github.com')) {

        $('#twitter-profile').remove();
        $('#dribbble-profile').remove();
        $('#instagram-profile').remove();
        $('.modal-backdrop').remove();
        adjustSelection('github-link');

        setupGithub(url, this);
      }
      else if (dribbble_integration_enabled && (url.attr('host') == 'dribbble.com' || url.attr('host') == 'www.dribbble.com')) {

         $('#twitter-profile').remove();
         $('#github-profile').remove();
         $('#instagram-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('dribbble-link');

         setupDribbble(url, this);
      }
      else {
         window.location = this.href;
      }
  });
}

function adjustSelection(el) {
  $('.main-nav').children('li').removeClass('sel');
  $('#' + el).parent().addClass('sel');
}

