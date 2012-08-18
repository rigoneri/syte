function setupOhloh(url, el) {
  var href = el.href;

  if ($('#ohloh-profile').length > 0) {
    window.location = href;
    return;
  }

  var params = url.attr('path').split('/').filter(function(w) {
    if (w.length) {
      return true;
    }
    return false;
  });

  if (params.length === 2) {
     var username = params[1];

     var spinner = new Spinner(spin_opts).spin();
     $('#ohloh-link').append(spinner.el);

     require(["json!/ohloh/" + username, "text!templates/ohloh-profile.html"],
        function(ohloh_data, ohloh_view) {
            if (ohloh_data.error || ohloh_data.length === 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(ohloh_view);
            ohloh_data.position = numberWithCommas(ohloh_data.position);
            ohloh_data.total_commits = numberWithCommas(ohloh_data.total_commits);
            ohloh_data.total_lines_changed = numberWithCommas(ohloh_data.total_lines_changed);

            $(template(ohloh_data)).modal().on('hidden', function () {
                $(this).remove();
                adjustSelection('home');
            });

            spinner.stop();

        });

     return;
  }

  window.location = href;
}
