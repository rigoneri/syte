
function setupSoundcloud(url, el) {
  var href = el.href;

  if ($('#soundcloud-profile').length > 0) {
    window.location = href;
    return;
  }

  var params = url.attr('path').split('/').filter(function(w) {
    if (w.length)
      return true;
    return false;
  });

  if (params.length == 1) {
    var username = params[0],
         spinner = new Spinner(spin_opts).spin();

    $('#soundcloud-link').append(spinner.el);

    require(["json!/soundcloud/" + username, "text!templates/soundcloud-profile.html"],
      function(soundcloud_data, soundcloud_view) {
        if (soundcloud_data.error || soundcloud_data.length == 0) {
          window.location = href;
          return;
        }
        var template = Handlebars.compile(soundcloud_view);

        $(template(soundcloud_data)).modal().on('hidden', function () {
          $(this).remove();
          if (currSelection === 'soundcloud') {
            adjustSelection('home');
          }
        });
        spinner.stop();
    });
    return;
  }

  window.location = href;
}
