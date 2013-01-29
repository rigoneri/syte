
function setupGithub(url, el) {
  var href = el.href;

  if ($('#github-profile').length > 0) {
    window.location = href;
    return;
  }

  var params = url.attr('path').split('/').filter(function(w) {
      if (w.length)
          return true;
      return false;
  })

  if (params.length == 1) {
     var username = params[0];

     var spinner = new Spinner(spin_opts).spin();
     $('#github-link').append(spinner.el);

     require(["json!/github/" + username, "text!templates/github-profile.html"],
        function(github_data, github_view) {
            if (github_data.error || github_data.length == 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(github_view);
            github_data.user.following = numberWithCommas(github_data.user.following)
            github_data.user.followers = numberWithCommas(github_data.user.followers)

            $(template(github_data)).modal().on('hidden', function () {
                $(this).remove();
                if (currSelection === 'github') {
                  adjustSelection('home');
                }
            })

            spinner.stop();

        });

     return;
  }

  window.location = href;
}
