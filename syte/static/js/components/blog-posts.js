
/** renderBlogPosts
 *
 * Takes the response from the blog platform and renders it using
 * our Handlebars template.
 */
function renderBlogPosts(posts) {
  if (posts.length === 0) {
      reachedEnd = true;
  }
  
  //Update this every time there are changes to the required 
  //templates since it's cached every time
  require.config({
    urlArgs: "bust=v2" 
  })

  require(["text!templates/blog-post-text.html",
          "text!templates/blog-post-photo.html",
          "text!templates/blog-post-link.html",
          "text!templates/blog-post-video.html",
          "text!templates/blog-post-audio.html",
          "text!templates/blog-post-quote.html"],

     function(text_post_template, photo_post_template,
              link_post_template, video_post_template,
              audio_post_template, quote_post_template) {

        var text_template = Handlebars.compile(text_post_template),
            photo_template = Handlebars.compile(photo_post_template),
            link_template = Handlebars.compile(link_post_template),
            video_template = Handlebars.compile(video_post_template),
            audio_template = Handlebars.compile(audio_post_template),
            quote_template = Handlebars.compile(quote_post_template);

        $('.loading').remove();
        $.each(posts, function(i, p) {
            p.formated_date = moment.utc(p.date, 'YYYY-MM-DD HH:mm:ss').local().format('MMMM DD, YYYY')

            if (disqus_integration_enabled)
                p.disqus_enabled = true;

            if (p.type == 'text') {
                var idx = p.body.indexOf('<!-- more -->');
                if (idx > 0) {
                    p.body = p.body.substring(0, idx)
                    p.show_more = true;
                }
                $('#blog-posts').append(text_template(p));
            }
            else if (p.type == 'photo')
                $('#blog-posts').append(photo_template(p));
            else if (p.type == 'link')
                $('#blog-posts').append(link_template(p));
            else if (p.type == 'video')
                $('#blog-posts').append(video_template(p));
            else if (p.type == 'audio')
                $('#blog-posts').append(audio_template(p));
            else if (p.type == 'quote')
                $('#blog-posts').append(quote_template(p));

        });

        adjustBlogHeaders();
        prettyPrint();
        setTimeout(setupBlogHeaderScroll, 1000);
        adjustSelection('home');

        $('body').trigger("blog-post-loaded");
     });
}

function fetchTumblrBlogPosts(offset, tag) {
  var blog_fetch_url = '/blog.json?o=' + offset;

  if (tag)
      blog_fetch_url = '/tags/' + tag + '/?o=' + offset;

  $.getJSON(blog_fetch_url, function(blog_posts) {
    renderBlogPosts(blog_posts.response.posts);
  });
}

function fetchWordpressBlogPosts(offset, tag) {
  var wpApiUrl = ['https://public-api.wordpress.com/rest/v1/sites/', wpDomain, '/posts/?callback=?'].join('');

  if (offset > 0) {
    wpApiUrl += '&offset=' + offset;
  }
  if (tag) {
    wpApiUrl += '&tag=' + tag.replace(/\s/g, '-');
  }

  $.getJSON(wpApiUrl, function(data) {
    // Get the data into a similar format as Tumblr so we can reuse the template
    $.each(data.posts, function(i, p) {
        var newTags = [];
        p.id = p.ID;
        p.body = p.content;
        p.content = null;
        if (p.type === 'post') {
          p.type = 'text';
        }
        for (tag in p.tags) {
          newTags.push(tag);
        }
        p.tags = newTags;
        // TODO: figure out how to preserve timezone info and make it consistent with
        // python's datetime.strptime
        if (p.date.lastIndexOf('+') > 0) {
          p.date = p.date.substring(0, p.date.indexOf('+'));
        }
        else {
          p.date = p.date.substring(0, p.date.indexOf('-'));
        }
    });
    renderBlogPosts(data.posts);
  });
}

/**
 * fetchBlogPosts
 *
 * @param offset Number The offset at which to start loading posts.
 * @param tag String Optional argument to specify to load posts with a certain tag.
 * @param platform String Optional argument to specify which blog platform to fetch from. Defaults to 'tumblr'.
 */
function fetchBlogPosts(offset, tag, platform) {
  if (platform === 'wordpress') {
      fetchWordpressBlogPosts(offset, tag);
  }
  else {
      // set default platform as Tumblr
      fetchTumblrBlogPosts(offset, tag);
  }
}

function adjustBlogHeaders() {
  if(isMobileView)
    return;

  $('.blog-section article hgroup').each(function(i, e) {
    $(e).find('h3 a').css({
       'margin-top': '-' + ($(e).height() + 100) + 'px'
    }).addClass('adjusted');
  });
}

function setupBlogHeaderScroll() {

  if(isMobileView)
    return;

  var previousTarget,
      activeTarget,
      $window = $(window),
      offsets = [],
      targets = [],
      $posts = $('.blog-section article hgroup h3 a').each(function() {
        if (this.hash) {
          targets.push(this.hash);
          offsets.push($(this.hash).offset().top);
        }
      });

  function processScroll(e) {
    var scrollTop = $window.scrollTop(),
        i = offsets.length;

    for (i; i--;) {
      if (activeTarget != targets[i] && scrollTop > offsets[i] && (!offsets[i + 1] || scrollTop < offsets[i + 1])) {

          var hgroup = $(activeTarget).find("hgroup");
          var margintop = '';
          if (hgroup.length) {
            margintop = '-' + ($(hgroup[0]).height() + 100) + 'px';
          }

          //set current target to be absolute
          $("h3 a[href=" + activeTarget + "]").removeClass("active").css({
            position: "absolute",
            top: "auto",
            'margin-top': margintop
          });

          //set new target to be fixed
          activeTarget = targets[i];
          $("h3 a[href=" + activeTarget + "]").attr('style', '').addClass("active");
      }

      if (activeTarget && activeTarget != targets[i] && scrollTop + 50 >= offsets[i] && (!offsets[i + 1] || scrollTop + 50 <= offsets[i + 1])) {

          // if it's close to the new target scroll the current target up
          $("h3 a[href=" + activeTarget + "]")
              .removeClass("active")
              .css({
                  position: "absolute",
                  top: ($(activeTarget).outerHeight(true) + $(activeTarget).offset().top - 50) + "px",
                  bottom: "auto"
              });
      }

      if (activeTarget == targets[i] && scrollTop > offsets[i] - 50  && (!offsets[i + 1] || scrollTop <= offsets[i + 1] - 50)) {
          // if the current target is not fixed make it fixed.
          if (!$("h3 a[href=" + activeTarget + "]").hasClass("active")) {
              $("h3 a[href=" + activeTarget + "]").attr('style', '').addClass("active");
          }
      }
    }
  }

  $posts.click(function(e) {
    if (!this.hash)
      return;
    $('html, body').stop().animate({
        scrollTop: $(this.hash).offset().top
    }, 500, 'linear');

    processScroll();
    e.preventDefault();
  });

  $window.scroll(processScroll).trigger("scroll");
}
