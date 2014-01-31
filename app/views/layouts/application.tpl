<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="web based media center">
    <meta name="author" content="pydeo">
    <link rel="shortcut icon" href="/img/favicon.png">

    <title>Pydeo</title>

    <link href="/css/lib/bootstrap.min.css" rel="stylesheet" type="text/css">
<!--     <link href="/css/lib/bootstrap-theme.min.css" rel="stylesheet" type="text/css"> -->
    <link href="/css/lib/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="/css/lib/video-js.min.css" rel="stylesheet" type="text/css">
    <link href="/css/style.css" rel="stylesheet" type="text/css">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/js/html5shiv.js"></script>
      <script src="/js/respond.min.js"></script>
    <![endif]-->

    <script type="text/javascript" src="/js/lib/jquery.min.js"></script>
  </head>

  <body>
    <!-- Wrap all page content here -->
    <div id="wrap">

        <!-- Fixed navbar -->
        <div class="navbar navbar-default navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="/">Pydeo</a>
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <!--  <li><a href="/music">Music</a></li> -->
                <li><a href="/movies">Movies</a></li>
                <!-- <li><a href="/series">Series</a></li> -->
              </ul>
              <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-cog fa-lg"></i></a>
                  <ul class="dropdown-menu">
                    <li><a href="/settings">Settings</a></li>
                    <!--
                    <li class="divider"></li>
                    <li class="dropdown-header">Nav header</li>
                    <li><a href="#">Separated link</a></li>
                    -->
                  </ul>
                </li>
              </ul>
              <form id="searchbar" class="navbar-form navbar-right form-search" role="search">
                  <div class="form-group">
                      <input type="text" class="form-control search-query" placeholder="Search..."/>
                  </div>
              </form>
            </div><!--/.nav-collapse -->
          </div>
        </div>

        <div class="container">
            <div id="notification"></div>
            <!-- content goes here, inside this container -->
            ${self.body()}
        </div> <!-- /container -->
    </div> <!-- wrap -->
    <div id="footer">
      <div class="container">
	<a href="http://projects.gw-computing.net/projects/pydeo/">Pydeo project</a>
      </div>
    </div>

    <script type="text/javascript" src="/js/lib/video.js"></script>
    <script>videojs.options.flash.swf = "/swf/video-js.swf"</script>
    <script type="text/javascript">
      document.createElement('video');document.createElement('audio');
    </script>
    <script type="text/javascript" src="/js/lib/jquery.validate.min.js"></script>
    <script type="text/javascript" src="/js/lib/bootstrap.min.js"></script>
    <script type="text/javascript" src="/js/scripts.js"></script>
  </body>
</html>
