Installation and Setup
======================

Install ``testapp``::

    $ git clone git://github.com/t0ster/django-gae-buildout-skeleton.git
    $ cd django-gae-buildout-skeleton
    $ python bootstrap.py
    $ ./bin/buildout

Update app.yaml and change application option to match your app name.

Update gae_main.py and change "testapp" to your project dir.

Deploy on GAE::

    $ ./bin/django deploy
