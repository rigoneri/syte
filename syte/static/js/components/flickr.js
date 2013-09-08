var flickr_template;
var flickr_spinner;

function setupFlickr(el) {
  var href = el.href;

  if($('#flickr-profile').length > 0) {
    window.location = href;
    return;
  }

  flickr_spinner = new Spinner(spin_opts).spin();
  $('#flickr-link').append(flickr_spinner.el);

  require(["text!templates/flickr-view.html?test=2"],
     function(flickr_view) {
        flickr_template = flickr_view;

         $.ajax({
            url: "http://api.flickr.com/services/feeds/photos_public.gne?id="+flickr_id+"&format=json&lang=en-us&jsoncallback=processFlickr",
            type: 'GET',
            dataType: 'jsonp'
        });


     });
}

function processFlickr(flickr_data) {
    var $modal;
    var template = Handlebars.compile(flickr_template);

    if (flickr_data.items == 0){
        window.location = href;
        return;
    }

    flickr_data.title = flickr_data.title.substring(13);

    //var d = new Date();
    $.each(flickr_data.items, function(i, p) {
        p.formated_date = moment.unix(Date.parse(p.date_taken)/1000).fromNow();
    });

    $modal = $(template(flickr_data)).modal().on('hidden', function () {
        $(this).remove();
        if (currSelection === 'flickr') {
            adjustSelection('home');
        }
    });

    flickr_spinner.stop();
}