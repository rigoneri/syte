
function setupLinks() {

  $('a').click(function(e) {
      e.preventDefault();
      e.stopPropagation();

      var url = $.url(this.href.replace('/#!', ''));

      if (this.id == 'home-link' && window.location.pathname == '/') {
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('home-link');
      }
      else if (this.id == 'apps-link') {
         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('#twitter-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('apps-link');

         var spinner = new Spinner(spin_opts).spin();
         $('#apps-link').append(spinner.el);

         require(["text!templates/apps-view.html"],
            function(apps_view) {
              $(apps_view).modal().on('hidden', function () {
                $(this).remove();
                adjustSelection('home-link');
              })
              spinner.stop();
            });
      }
      else if (twitter_integration_enabled && (url.attr('host') == 'twitter.com' || url.attr('host') == 'www.twitter.com')) {

         $('#github-profile').remove();
         $('#dribbble-profile').remove();
         $('.modal-backdrop').remove();
         adjustSelection('twitter-link');

         setupTwitter(url, this);
      }
      else if (github_integration_enabled && (url.attr('host') == 'github.com' || url.attr('host') == 'www.github.com')) {

        $('#twitter-profile').remove();
        $('#dribbble-profile').remove();
        $('.modal-backdrop').remove();
        adjustSelection('github-link');

        setupGithub(url, this);
      }
      else if (dribbble_integration_enabled && (url.attr('host') == 'dribbble.com' || url.attr('host') == 'www.dribbble.com')) {

         $('#twitter-profile').remove();
         $('#github-profile').remove();
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

