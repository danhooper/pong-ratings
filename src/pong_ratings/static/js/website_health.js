var WebsiteHealth = {
    init: function() {
        $(document).on('click', '.result-expand', 
        		WebsiteHealth.resultExpand);
    },
    healthCheck: function() {
        var numGood = 0;
        var numBad = 0;
        $('.website_health_link').each(function(index, elem) {
            postData = {link_url: $(this).data('link-url')};
            $.post('website_health/health/', postData, function(data) {
                try{ 
                    if ( data['health']) {
                        numGood += 1
                        $(elem).appendTo('#website_good_pages');
                    } else {
                        numBad += 1;
                    }
                    $(elem).children('.result').text(data['health']);
                } catch(err) {
                    console.log('[.website_health_link] ' + err)
                    numBad += 1;
                    $(elem).children('.result').text('Error');
                }
                $('#website_health_report').html('Good ' + numGood + '<br/>Bad: ' + numBad)
            })
        })
    },
    resultExpand: function() {
        event.preventDefault();
        target_a = event.target;
        if ($(event.target).is('i')) {
            target_a = $(event.target).parent();
        }
        resultDiv = $(target_a).nextAll('.result').slice(0,1);
        if( resultDiv.hasClass('hidden')) {
            $(resultDiv).css('display', 'block');
            $(resultDiv).addClass('visible');
            $(resultDiv).removeClass('hidden');
            $(target_a).children('.icon-plus').addClass('icon-minus');
            $(target_a).children('.icon-plus').removeClass('icon-plus');
        } else {
            $(resultDiv).css('display', 'none');
            $(resultDiv).addClass('hidden');
            $(resultDiv).removeClass('visible');
            $(target_a).children('.icon-minus').addClass('icon-plus');
            $(target_a).children('.icon-minus').removeClass('icon-minus');
        }
        
    }
};