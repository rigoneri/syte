
function setupBitbucket(url, el) {
  var href = el.href;

  if ($('#bitbucket-profile').length > 0) {
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
     $('#bitbucket-link').append(spinner.el);

     require(["json!/bitbucket/" + username, "text!templates/bitbucket-profile.html"],
        function(bitbucket_data, bitbucket_view) {
            if (bitbucket_data.error || bitbucket_data.length == 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(bitbucket_view);
            bitbucket_data.user.followers = numberWithCommas(bitbucket_data.user.followers)

            $(template(bitbucket_data)).modal().on('hidden', function () {
                $(this).remove();
                if (currSelection === 'bitbucket') {
                  adjustSelection('home');
                }
            })

            spinner.stop();

        });

     return;
  }

  window.location = href;
}
