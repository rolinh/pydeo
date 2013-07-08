$(document).ready(function () {
    // mark menu as active when clicked
    $('ul.nav > li > a[href="' + document.location.pathname + '"]').parent().addClass('active');
});
