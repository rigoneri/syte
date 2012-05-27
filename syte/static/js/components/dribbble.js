
function setupDribbble(url, el) {
  var href = el.href;

  if ($('#dribbble-profile').length > 0) {
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
     $('#dribbble-link').append(spinner.el);

     require(["json!/dribbble/" + username, "text!templates/dribbble-view.html"],
        function(dribbble_data, dribbble_view) {
            if (dribbble_data.message || dribbble_data.length == 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(dribbble_view);

            var user = dribbble_data.shots[0].player;
            user.following_count = numberWithCommas(user.following_count);
            user.followers_count = numberWithCommas(user.followers_count);
            user.likes_count = numberWithCommas(user.likes_count);

            var template_data = {
                "user": user,
                "shots": dribbble_data.shots
            }

            $(template(template_data)).modal().on('hidden', function () {
                $(this).remove();
                adjustSelection('home-link');
            })

            spinner.stop();
        });

     return;
  }

  window.location = href;
}
