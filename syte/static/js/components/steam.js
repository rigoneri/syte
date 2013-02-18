
function setupSteam(url, el) {
  var href = el.href;

  if ($('#steam-profile').length > 0) {
    window.location = href;
    return;
  }

  var params = url.attr('path').split('/').filter(function(w) {
      if (w.length)
          return true;
      return false;
  })

  if (params.length == 2) {
     var username = params[1];

     var spinner = new Spinner(spin_opts).spin();
     $('#steam-link').append(spinner.el);

     require(["json!/steam/" + username, "text!templates/steam-profile.html"],
        function(steam_data, steam_view) {
            if (steam_data.error || steam_data.length == 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(steam_view);

            var template_data = {
                "user": steam_data.user,
                "recent_games": steam_data.recent_games
            }

            $(template(template_data)).modal().on('hidden', function () {
                $(this).remove();
                if (currSelection === 'steam') {
                  adjustSelection('home');
                }
            })

            spinner.stop();
        });

     return;
  }

  window.location = href;
}
