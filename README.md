# PYDEO

[![Build Status](https://travis-ci.org/Rolinh/pydeo.png?branch=master)](https://travis-ci.org/Rolinh/pydeo)
[![Dependencies Status](https://gemnasium.com/Rolinh/pydeo.png)](https://gemnasium.com/Rolinh/pydeo)

**pydeo** is a web based media center. When completed, it will allow you to
watch your movies or series episodes in streaming through an HTML5 video player
(with a flash player fallback if HTML5 video is not possible) or directly on the
computer on which **pydeo** is installed. Other features will include playing
music or access complete movie description with trailer, list of actores and so
on.

It is written in `python` using the [bottle](http://bottlepy.org/docs/stable/)
framework. Its main goals are to be simple, lightweight and easy to the eyes.
Therefore, it should run on very low power platforms which makes it ideal for
micro computers such as the Raspberry Pi.

**pydeo** uses [twitter bootstrap](http://getbootstrap.com/) and
[jquery](http://jquery.com/) to make the interface look nice and ease my pain in
creating a beautiful UI (yeah, I'm not a designer guy, just a simple developer).

## DISCLAIMER

There is no release yet as I just started the project. My goal is to rapidly
release a version with very few features and improve it over time.

## INSTALLATION

First thing you need is `python` (version 3.3).

Once you have `python`, you need to install `bottle`. There are several way to
achieve this. Here is the one I use and recommend:

* install `virtualenv` and `pip` if necessary
* set up a virtual environment: `virtualenv -p python env` (replace `python`
  with `python3.3` if `python` 3.3 is not your default `python` version)
* activate it: `source env/bin/activate`
* install the required libraries through `pip`:
  `pip install -r requirements.txt`
* initialize the submodules: `invoke init_submodules`
* if you set up **pydeo** as described in basic configuration section, install
  `cherrypy`:
  `pip install cherrypy`
  otherwise, install the appropriate server backend corresponding to the one you
  set up in the `settings.py` file

Once done, follow the instructions from the settings section.

## SETTINGS

### BASIC CONFIGURATION

Run the following command to set default settings (should be fine for most
users):

    invoke setup

Then, simply run `run.py`:

    python run.py

Open your browser and navigate to <http://localhost:8080>.

### ADVANCED CONFIGURATION

Run the following command to set default settings:

    invoke setup

Then, adjust the settings as you like in `pydeo/config/settings.py`.
Some of the possible server backends are the following:

* cherrypy
* gunicorn
* tornado
* waitress

The theory is that every server backend supported by the `bottle` framework that
also supports `python 3.3` should be fine. Have a look at
[bottle documentation](http://bottlepy.org/docs/stable/deployment.html#switching-the-server-backend)
for the full list. However, I haven't tested all of them of course.

Adjust `sqlalchemy.url` in `alembic.ini` file if you do not intend to use
[SQLite](http://www.sqlite.org/). If you modify this line, set the same database
URL in `pydeo/config/settings.py`.

Supported databases are the ones supported by
[SQLAlchemy](http://www.sqlalchemy.org/):

* Drizzle
* Firebird
* Informix
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* SQLite
* Sybase

Example URL for for `MySQL`: `mysql://pydeo:pydeo_passwd@localhost/pydeo`.

In any case, remember that unless your movie database contains hundreds of
thousands of files, you should be good with `SQLite`.

## ADDING FILES

You need to add you media files in the `files` folder of **pydeo**. It expects
the following structure:
<pre>
files
|__music
|    |__example_artist
|           |__example_album
|                 |__example_track.flac
|__movies
|    |__ example_movie.mkv
|__series
     |__example_serie
           |__season01
           |     |__episode01.mkv
           |__season02
                 |__ episode02.mkv
</pre>

So add your movies in a `movies` folder and so on. If you do not want to copy
all your media files in these directories, I suggest you use symbolic links
(this is actually the way I would recommend).

## CONTRIBUTING

Any contribution that improves **pydeo** is welcome. :)
Feel free to contact me if you have any question or suggestion.

If you already have developed with the Ruby on Rails framework, you should then
be familiar with how I organised the sources. If not but you are familiar with
the MVC pattern, you should be fine too.

**pydeo** is based around a JSON REST API, available under `/api` URL. It makes
it easy to fetch information for `javascript` processing. It also has the
advantage of processing more stuff on the client side rather than on the server
side.

If you want to submit patches, you need to make sure your changes pass the
tests. Think about updating the tests if necessary. But before that, install the
requirements to run the tests:

    pip install -r requirements_dev.txt

Once done, make sure all tests pass by running `invoke test`.
Make also sure your additions are conform to PEP8 by running `invoke pep8`.
