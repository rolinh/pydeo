/**
 * Create a table with the list of movies for /movies page.
 */
function loadMoviesList() { 
    $.ajax({
       url: '/api/movies',
       dataType: 'json',
       type: 'GET',
       async: 'true',
       success: function(data) {
           $.each(data, function(i,v) {
               var row = '<tr>';
               row += '<td class="right"><a href="movies/' + v['id'] + '/play"><i class="fa fa-play"></i></a></td>';
               row += '<td><a href="movies/' + v['id'] + '">' + v['title'] + '</a></td>';
               row += '<td>' + v['year'] + '</td>';
               row += '<td>' + v['genres'] + '</td>';
               row += '<td>' + v['rating'] + ' / 10</td>';
               row += '<td>' + v['runtime'] + ' </td>';
               row += '</tr>';
               $('#movies-list').append(row);
           });
       },
       error: function(jqXHR, textStatus, errorThrown) {
            $('#notification').html('<div class="alert alert-danger alert-dismissable">\
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
                <strong>Error! </strong>' + textStatus + '</div>');
       }
   });
}

/**
 * Display a movie in the page /movies/<id>
 */
function displayMovie(id) {
    $.ajax({
        url: '/api/movies/' + id,
        dataType: 'json',
        type: 'GET',
        async: 'true',
        success: function(movie) {
            $('#play').attr('href', '/movies/' + movie.id + '/play');
            $.each(movie, function(k,v) {
				if ($('[data-key=' + k + ']').length > 0) {
					$('[data-key=' + k + ']').prepend(v);
				} else if (k === 'cover_url') {
					$('[data-image=cover]').attr('src', v);
				} else if (k === 'trailers') {
					$('#accordion').html(createAccordion(v));
				}
            });
            /*
			videojs("trailer", {}, function(){
				// Player (this) is initialized and ready.
			});
            */
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#notification').html('<div class="alert alert-danger alert-dismissable">\
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
                <strong>Error! </strong>' + textStatus + '</div>');
       }
    });
}

/**
 * Display movie play page.
 */
function displayMoviePlay(id) {
    $.ajax({
        url: '/api/movies/' + id,
        dataType: 'json',
        type: 'GET',
        async: 'true',
        success: function(movie) {
            $('[data-key=title]').text(movie.title);
			$('[data-video=movie]').html('<source src="/' + movie.file_path + '" type="' + movie.mime_type + '" />');
			videojs("movie", {}, function(){
				// Player (this) is initialized and ready.
			});
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#notification').html('<div class="alert alert-danger alert-dismissable">\
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
                <strong>Error! </strong>' + textStatus + '</div>');
        }
    });
}

/**
 * Take a comma separated list of URLs, in this form: format#url
 * Then, render an accordion with movie trailers based on the URL.
 */
function createAccordion(urlList) {
	/* in case there is no trailers */
	if (urlList === '') {
		return '';
	}
	var panel = '';
	var trailers = urlList.split(',');
	
	for (i in trailers) {
		var tmp = trailers[i].split('#');
		var format = tmp[0];
		var url = tmp[1];
		var ind = parseInt(i) + 1;
		panel += '<div class="panel panel-default">';
		panel += '<div class="panel-heading">';
		panel += '<h4 class="panel-title">';
		panel += '<a data-toggle="collapse" data-parent="#accordion" href="#trailer' + ind + '">Trailer #' + ind + '</a>';
		panel += '</h4>';
		panel += '</div>';
		panel += '<div id="trailer' + ind + '" class="panel-collapse collapse">';
		panel += '<div class="panel-body">';
		panel += url;
		panel += '</div>';
		panel += '</div>';
		panel += '</div>';
	}

	return panel;
}

