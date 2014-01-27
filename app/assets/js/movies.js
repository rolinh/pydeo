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
               row += '<td>' + v['rating'] + '</td>';
               row += '<td>' + v['runtime'] + '</td>';
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
                $('[data-key=' + k + ']').text(v);
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#notification').html('<div class="alert alert-danger alert-dismissable">\
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
                <strong>Error! </strong>' + textStatus + '</div>');
       }
    });
}
