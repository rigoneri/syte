
function setupTwitter(url, el) {
  var href = el.href;

  if ($('#twitter-profile').length > 0) {
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
     $('#twitter-link').append(spinner.el);

     require(["json!/twitter/" + username, "text!templates/twitter-view.html"], 
        function(twitter_data, twitter_view) {
            if (twitter_data.error || twitter_data.length == 0) {
                window.location = href;
                return;
            }

            var template = Handlebars.compile(twitter_view);

            var tweets = [];
            $.each(twitter_data, function(i, t) {
              if (i > 3)
                return;

              //'ddd MMM DD HH:mm:ss ZZ YYYY'
              t.formated_date = moment(t.created_at).fromNow();
              t.f_text = twitterLinkify(t.text);
              tweets.push(t);
            });

            var user = twitter_data[0].user;
            user.statuses_count = numberWithCommas(user.statuses_count);
            user.friends_count = numberWithCommas(user.friends_count);
            user.followers_count = numberWithCommas(user.followers_count);
            user.f_description = twitterLinkify(user.description);

            var template_data = {
                "user": user,
                "tweets": tweets
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

function twitterLinkify(text) {
  text = text.replace(/(https?:\/\/\S+)/gi, function (s) {
    return '<a href="' + s + '">' + s + '</a>';
  });

  text = text.replace(/(^|) @(\w+)/gi, function (s) {
    return '<a href="http://twitter.com/' + s + '">' + s + '</a>';
  });

  text = text.replace(/(^|) #(\w+)/gi, function (s) {
    return '<a href="http://search.twitter.com/search?q=' + s.replace(/#/,'%23') + '">' + s + '</a>';
  });

  return text;
}

