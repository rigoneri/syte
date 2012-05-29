
var isMobileView = false;
var mediaQuery = window.matchMedia("(max-width:600px)");

if (mediaQuery.matches) {
    isMobileView = true;
}

$(function() {
  $('#mobile-nav-btn').click(function() {
     $('.main-section').toggleClass('nav-opened');
  });
});


