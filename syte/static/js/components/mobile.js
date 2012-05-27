
var isMobileView = false;
var mediaQuery = window.matchMedia("(max-width:600px)");

if (mediaQuery.matches) {
    isMobileView = true;
}

$(function() {
    $('body').append(
      '<div class="mobile-nav">' +
        '<span class="nav-btn" id="mobile-nav-btn">' +
          '<span class="nav-btn-bar"></span>' +
          '<span class="nav-btn-bar"></span>' +
          '<span class="nav-btn-bar"></span>' +
        '</span>' +
        '<h3><a href="/">rigoneri.com</a></h3>' +
      '</div>');

    $('#mobile-nav-btn').click(function() {
       $('.main-section').toggleClass('nav-opened');
    });
});


