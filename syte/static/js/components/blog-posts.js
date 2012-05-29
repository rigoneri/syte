
function fetchBlogPosts(post, tag) {
  var blog_fetch_url = '/blog.json';

  if (post)
      blog_fetch_url = '/post/' + post;
  else if (tag)
      blog_fetch_url = '/tags/' + tag;

  $.getJSON(blog_fetch_url, function(blog_posts) {
      require(["text!templates/blog-post-text.html",
              "text!templates/blog-post-photo.html",
              "text!templates/blog-post-link.html",
              "text!templates/blog-post-video.html",
              "text!templates/blog-post-audio.html",
              "text!templates/blog-post-quote.html"],

         function(text_post_template, photo_post_template, 
                  link_post_template, video_post_template, audio_post_template,
                  quote_post_template) {

            var text_template = Handlebars.compile(text_post_template);
            var photo_template = Handlebars.compile(photo_post_template);
            var link_template = Handlebars.compile(link_post_template);
            var video_template = Handlebars.compile(video_post_template);
            var audio_template = Handlebars.compile(audio_post_template);
            var quote_template = Handlebars.compile(quote_post_template);

            $('.loading').remove();
            $.each(blog_posts.response.posts, function(i, p) {
                p.formated_date = moment(p.date).format('MMMM DD, YYYY')

                if (p.type == 'text')
                    $('#blog-posts').append(text_template(p));
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

            setupLinks();
            adjustBlogHeaders();
            prettyPrint();
            setTimeout(setupBlogHeaderScroll, 1000);
            adjustSelection('home-link');
         });
  });
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
