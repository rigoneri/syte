
function setupTent(el) {
  var href = el.href;

  if ($('#tent-profile').length > 0) {
    window.location = href;
    return;
  }

  var spinner = new Spinner(spin_opts).spin();
  $('#tent-link').append(spinner.el);

  require(
    ["json!" + tent_entity_uri + "/posts",
     "json!" + tent_entity_uri + "/profile",
     "json!" + tent_entity_uri + "/followers",
     "json!" + tent_entity_uri + "/followings", 
     "json!" + tent_entity_uri + "/posts/count",
     "text!templates/tent-view.html"],

    function(tent_posts, tent_profile, tent_followers, tent_followings, tent_posts_count, tent_view) {

      if (tent_posts.error || tent_posts.length == 0) {
        window.location = href;
          return;
        }

      var template = Handlebars.compile(tent_view);


      var user = tent_profile["https://tent.io/types/info/basic/v0.1.0"];

      user.entity_url = tent_profile["https://tent.io/types/info/core/v0.1.0"].entity;
      user.feed_url = tent_feed_url;
      user.profile_image_url = user.avatar_url;
      user.statuses_count =numberWithCommas(tent_posts_count);
      user.friends_count = numberWithCommas(tent_followings.length);
      user.followers_count = numberWithCommas(tent_followers.length);
      user.f_description =  user.bio;

      var posts = [];
      var item_count = 0;
      $.each(tent_posts, function(i, t) {
        if (item_count > 4)
          return;

        // show only tent.io status posts
        if (t.type == "https://tent.io/types/post/status/v0.1.0") {
          t.formated_date = moment(new Date(t.published_at * 1000)).fromNow();
          t.f_text = tentLinkify(t.content.text);
          t.user = user;
          posts.push(t);
          item_count++;
        }
      });

      var template_data = {
        "user": user,
        "posts": posts
      }

      $(template(template_data)).modal().on('hidden', function () {
        $(this).remove();
        if (currSelection === 'tent') {
          adjustSelection('home');
        }
      })

    spinner.stop();
    });

}

function tentLinkify(text) {
  text = text.replace(/(https?:\/\/\S+)/gi, function (s) {
    return '<a href="' + s + '">' + s + '</a>';
  });

  return text;
}
