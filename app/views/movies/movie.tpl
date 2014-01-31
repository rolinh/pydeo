<%inherit file="../layouts/application.tpl"/>
<div class="row">
	<div class="col-md-3"></div>
	<div class="col-md-9 center">
		<h4 data-key="title"> (<span data-key="year"></span>)</h4>
	</div>
</div>
<div class="row">
    <div class="col-md-3 center">
		<img data-image="cover" class="round-corners" src=""/>
    </div>
    <div class="col-md-9">
		<table class="table">
			<tr>
				<td><strong>Runtime: </strong></td>
				<td data-key="runtime"> minutes</td>
			</tr>
			<tr>
			<td><strong>Genres: </strong></td>
			<td data-key="genres"></td>
			</tr>
			<tr>
			<td><strong>Certification: </strong></td>
			<td data-key="certification"></td>
			</tr>
			<tr>
			<td><strong>Directors: </strong></td>
			<td data-key="directors"></td>
			</tr>
			<tr>
			<td><strong>Writers: </strong></td>
			<td data-key="writers"></td>
			</tr>
			<tr>
			<td><strong>Cast: </strong></td>
			<td data-key="cast"></td>
			</tr>
		</table>
    </div>
</div>
<div class="row top-10">
	<div class="panel panel-default">
		<div class="panel-heading">Plot</div>
		<div data-key="plot_outline" class="panel-body"></div>
	</div>
</div>
<div class="row">
	<div class="panel-group" id="accordion"></div>
</div>

<script type="text/javascript" src="/js/movies.js"></script>
<script type="text/javascript">displayMovie(${id})</script>
