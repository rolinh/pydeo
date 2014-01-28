function loadMoviesList() { 
    $.ajax({
       url: '/api/movies',
       dataType: 'json',
       method: 'get',
       async: 'true',
       success: function(data) {
           $.each(data, function(i,v) {
               var row = '<tr>';
               row += '<td><a href="movies/id/' + v['id'] + '">' + v['title'] + '</a></td>';
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

function displayMovie(id) {
    $.ajax({
        url: '/api/movies/id/' + id,
        dataType: 'json',
        method: 'get',
        async: 'true',
        success: function(movie) {
            $.each(movie, function(k,v) {
				if ($('[data-key=' + k + ']').length > 0) {
					$('[data-key=' + k + ']').prepend(v);
				} else if (k === 'cover_url') {
					$('[data-image=cover]').attr('src', v);
				} else if (k === 'file_path') {
					$('[data-video=movie]').html('<source src="/' + v + '" type="' + movie['mime_type'] + '" />');
				} else if (k === 'trailers') {
					$('#accordion').html(createAccordion(v));
				}
            });
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