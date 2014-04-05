var HomePage = {
    init: function () {
        $('#rss_feeds').load('rss_reader/', function() {
            $('.feed').each(function () {
                $(this).load($(this).data('url'));
            })
        });
        $('#website_health').load('website_health/', function() {
            $('.website').each(function () {
                $(this).load($(this).data('url'));
            })
        });
    },
};