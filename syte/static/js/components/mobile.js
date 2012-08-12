
var isMobileView = false;

if (typeof window.matchMedia !== 'undefined') {
    var mediaQuery = window.matchMedia("(max-width:799px)");
    if (mediaQuery.matches) {
        isMobileView = true;
    }
}

$(function() {
  $('#mobile-nav-btn').click(function() {
     $('.main-section').toggleClass('nav-opened');
  });
});


