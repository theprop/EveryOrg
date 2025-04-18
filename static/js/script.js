// static/js/script.js
$(document).ready(function() {
    $('.image-card').hover(
        function() {
            $(this).find('.overlay').css('opacity', 1);
        },
        function() {
            $(this).find('.overlay').css('opacity', 0);
        }
    );

    $('.image-card').click(function() {
        const cause = $(this).data('cause');
        const apiUrl = $(this).data('api-url');
        const $results = $('#nonprofit-results');
        $results.html('<p>Loading nonprofits for ' + cause + '...</p>');

        fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                $results.empty();
                const nonprofits = data.nonprofits || [];
                if (nonprofits.length === 0) {
                    $results.append(`<p>No nonprofits found for ${cause}</p>`);
                } else {
                    $results.append(`<h4>Nonprofits for ${cause.charAt(0).toUpperCase() + cause.slice(1)}</h4>`);
                    const $ul = $('<ul></ul>');
                    nonprofits.forEach(np => {
                        $ul.append(`<li><a href="https://www.every.org/${np.slug}#donate" target="_blank">${np.name}</a></li>`);
                    });
                    $results.append($ul);
                }
            })
            .catch(error => {
                console.error('Error fetching nonprofits:', error);
                $results.html(`<p>Failed to load nonprofits: ${error.message}</p>`);
            });
    });
});
