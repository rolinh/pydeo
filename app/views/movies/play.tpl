<%inherit file="../layouts/application.tpl"/>
<div class="row top-10">
	<div class="panel panel-default">
		<div data-key="title" class="panel-heading"></div>
		<div class="panel-body">
			<video id="movie" data-video="movie" class="round-corners video-js vjs-default-skin" controls preload="auto" data-setup="{}">
				
			</video>
		</div>
	</div>
</div>

<script type="text/javascript" src="/js/movies.js"></script>
<script type="text/javascript">displayMoviePlay(${id})</script>
