# PYDEO

[![Build Status](https://travis-ci.org/Rolinh/pydeo.png?branch=master)](https://travis-ci.org/Rolinh/pydeo)

**pydeo** is an application for managing media files such as movies, series and
music through a web browser.

It is written in `python` using the `bottle` framework. Its main goals are to be
simple, lightweight and easy to the eyes. Therefore, it should run on very low
power platforms which makes it ideal for micro computers such as the Raspberry
Pi.

**pydeo** uses `twitter bootstrap` and `jquery` to make the interface look nice
and ease my pain in creating a beautiful UI (yeah, I'm not a designer guy, just
a simple developer).

## DISCLAIMER

There is no release yet as I just started the project. My goal is to rapidly
release a version with very few features and improve it over time.

## TESTING THE APPLICATION

First thing you need is `python` (version 3.3).

Once you have `python`, you need to install `bottle`. There are several way to
achieve this. Here is the one I use and recommend:

* install `virtualenv` and `pip` if necessary
* set up a virtual environment: `virtualenv -p python .`
* activate it: `source bin/activate`
* install the required libraries through `pip`:
  `pip install -r requirements.txt`
* init submodules: `make init_submodules`

Copy `config/settings.py.sample` to `config/settings.py` and adjust the settings
if necessary.

Once done, you're ready and can simply run `pydeo.py`:

    python pydeo.py

Open your browser and navigate to `http://localhost:8080`.

## ADDING FILES

You need to add you media files in the `files` folder of **pydeo**. It expects
the following structure:
<pre>
files
|___audio
|   |__music
|       |__example_artist
|           |__example_album
|               |__example_track.flac
|__video
    |__movies
    |   |__ example_movie.mkv
    |__series
        |__example_serie
            |__season01
            |   |__episode01.mkv
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

If you want to submit patches, you need to make sure your changes pass the
tests. Think about updating the tests if necessary. But before that, install the
requirements to run the tests:

    pip install -r requirements_dev.txt

Once done, make sure all tests pass by running `make test_all`.

