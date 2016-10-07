This file is for you to describe the twa application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``twa`` using the setup.py script::

    $ sudo apt-get install libjpeg-dev libfreetype6-dev libfreetype6-dev zlib1g-dev
    $ cd twa
    $ pip install -e . --allow-external tw2.bootstrap.forms --pre --process-dependency-links --trusted-host github.com --trusted-host dobisel.com

Create the project database for any model classes defined::

    $ gearbox setup-app

Start the paste http server::

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ gearbox serve --reload --debug

Then you are ready to go.
