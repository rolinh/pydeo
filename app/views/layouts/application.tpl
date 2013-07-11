<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Pydeo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <!--link rel="stylesheet/less" href="less/bootstrap.less" type="text/css" /-->
        <!--link rel="stylesheet/less" href="less/responsive.less" type="text/css" /-->
        <!--script src="js/less-1.3.3.min.js"></script-->
        <!--append ‘#!watch’ to the browser URL, then refresh the page. -->

        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/bootstrap-responsive.min.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">

        <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
        <script src="js/html5shiv.js"></script>
        <![endif]-->

        <!-- Fav and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="img/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="img/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="img/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="img/apple-touch-icon-57-precomposed.png">
        <link rel="shortcut icon" href="img/favicon.png">

        <script type="text/javascript" src="js/jquery.min.js"></script>
        <script type="text/javascript" src="js/jquery.validate.min.js"></script>
        <script type="text/javascript" src="js/bootstrap.min.js"></script>
        <script type="text/javascript" src="js/bootbox.min.js"></script>
        <script type="text/javascript" src="js/scripts.js"></script>
    </head>

    <body>
        <!-- wrap is used to push the footer at the bottom -->
        <div id="wrap">
            <div class="container-fluid">
                <div class="row-fluid">
                    <div class="span12">
                        <div class="row-fluid">
                            <div class="span12">
                                <div class="page-header">
                                    <h1>
                                        Pydeo <small>Your media with ease</small>
                                    </h1>
                                </div> <!-- page-header -->
                            </div> <!-- span6 -->
                        </div> <!-- row-fluid -->
                        <!-- fixed navbar -->
                        <div class="navbar">
                            <div class="navbar-inner">
                                <div class="container-fluid">
                                    <a data-target=".navbar-responsive-collapse" data-toggle="collapse" class="btn btn-navbar"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></a> <a href="/" class="brand">Pydeo</a>
                                    <div class="nav-collapse collapse navbar-responsive-collapse">
                                        <ul class="nav">
                                            <li class="dropdown">
                                                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Audio <b class="caret"></b></a>
                                                <ul class="dropdown-menu">
                                                    <li>
                                                        <a href="/music">Music</a>
                                                    </li>
                                                </ul>
                                            </li>
                                            <li class="dropdown">
                                                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Video <b class="caret"></b></a>
                                                <ul class="dropdown-menu">
                                                    <li>
                                                        <a href="/movies">Movies</a>
                                                    </li>
                                                    <li>
                                                        <a href="/series">Series</a>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div> <!-- nav-collapse collapse navbar-responsive-collapse -->
                                </div> <!-- container-fluid -->
                            </div> <!-- navbar-inner -->
                        </div> <!-- navbar -->
                    </div> <!-- span12 -->
                </div> <!-- row-fluid -->
            </div> <!-- container-fluid -->

            <div class="container-fluid">
                <!-- content goes here, inside this container -->
                %include
            </div> <!-- container-fluid -->

            <!-- to push down the footer -->
            <div id="push"></div>
        </div> <!-- wrap -->
        <div id="footer">
            <div class="container">
                <p class="muted credit">Pydeo project <a href="http://projects.gw-computing.net/projects/pydeo">pydeo</a></p>
            </div> <!-- container -->
        </div> <!-- footer -->
    </body>
</html>
