var RssReader = {
    init: function () {
        $(document).on('click', '.feed-expand', RssReader.feedExpand);
    },
    feedExpand: function(event) {
        event.preventDefault();
        target_a = event.target;
        if ($(event.target).is('i')) {
            target_a = $(event.target).parent();
        }
        entry_wrapper = $(target_a).nextAll('.entry_wrapper').slice(0, 1);
        if (entry_wrapper.hasClass('hidden')) {
            console.log('Showing');
            $(entry_wrapper).css('display', 'block');
            $(entry_wrapper).addClass('visible');
            $(entry_wrapper).removeClass('hidden');
            $(target_a).children('.icon-plus').addClass('icon-minus');
            $(target_a).children('.icon-plus').removeClass('icon-plus');
        } else {
            console.log('Hiding');
            $(entry_wrapper).css('display', 'none');
            $(entry_wrapper).addClass('hidden');
            $(entry_wrapper).removeClass('visible');
            $(target_a).children('.icon-minus').addClass('icon-plus');
            $(target_a).children('.icon-minus').removeClass('icon-minus');    
        }
    },
};