
function setupLinkedin(url, el) {
  var href = el.href;

  if ($('#linkedin-profile').length > 0) {
    window.location = href;
    return;
  }

  var spinner = new Spinner(spin_opts).spin();
  $('#linkedin-link').append(spinner.el);

  require(["json!/linkedin/", "text!templates/linkedin-view.html"],
    function(linkedin_data, linkedin_view) {
        if (linkedin_data.error) {
            window.location = href;
            return;
        }

        var template = Handlebars.compile(linkedin_view);

        linkedin_data.profile['profile_url'] = 'http://linkedin.com/profile/view?id=' + linkedin_data.profile['id']
        linkedin_data.profile['numGroups'] = linkedin_data.groups['_count']
        linkedin_data.profile['numNetworkUpdates'] = linkedin_data.network_updates['_total']
        linkedin_data.profile['location_name'] = linkedin_data.profile['location']['name']

        $(template(linkedin_data)).modal().on('hidden', function () {
            $(this).remove();
            if (currSelection === 'linkedin') {
              adjustSelection('home');
            }
        })

        spinner.stop();
    });
}
