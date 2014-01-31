<%inherit file="../layouts/application.tpl"/>
<div class="table-responsive">
    <table class="table table-hover">
        <thead>
            <tr>
                <th  class="right">
                <a data-remote="true" data-spinnable="true" data-callback="loadMoviesList();" href="/api/movies/reload"><i class="fa fa-refresh"></i></a>
                </th>
                <th>
                   Title
                </th>
                <th>
                    Year
                </th>
                <th>
                    Genres
                </th>
                <th>
                    Rating
                </th>
                <th>
                    Runtime (mn)
                </th>
            </tr>
        </thead>
        <tbody id="movies-list">
        </tbody>
    </table>
</div>
<script type="text/javascript" src="/js/movies.js"></script>
<script type="text/javascript">loadMoviesList();</script>
