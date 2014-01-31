$(function () {
    /**
     * Mark menu elements from the navbar as active when clicked.
     */
    $('ul.nav > li > a[href="' + document.location.pathname + '"]').parent().addClass('active');

    /**
     * Perform a GET request asynchronously and calls a callback function if
     * defined in data-callback attribute. It also adds spinnable effect on
     * font-awesome icons if data-spinnable attribute is set to true.
     */
    $('a[data-remote=true]').click(function() {
        var isSpinnable = $('[data-spinnable=true]').length > 0;
        var callback = $(this).data('callback');
        var icon;

        if (isSpinnable) {
            icon = $(this).children('i');
            icon.addClass('fa-spin');
        }

        $.ajax({
            url: $(this).attr('href'),
            type: 'GET',
            async: 'true',
            success: function() {
                // TODO notify
            },
            error: function() {
                // TODO handle error
            },
            complete: function() {
                if (isSpinnable) {
                    setTimeout(function() {
                        icon.removeClass('fa-spin');
                    }, 1000);
                }

                if (callback !== undefined) {
                    eval(callback);
                }
            }
        });

        // block href redirection
        return false;
    })
});
