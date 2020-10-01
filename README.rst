

Modifications:

+ 0 at "input id" stage leads to downloading all items displayed.

+ --zip optional argument

+ --convert optional argument, converts all to pdf, requires calibre 'ebook-convert' cli with path set ; deletes original file format

+ --upload optinal argument, requires "MEGA_USER" & "MEGA_PASS" environment variable to be set, uploads files to new /books/<search_term> folder in MegaSync ; deletes local file


+TODO: fix for pip



libgen.py |PyPy Package| |Build Status| |License: MIT|
======================================================


A script to download books from gen.lib.rus.ec, libgen.io, libgen.pw, b-ok.org and bookfi.net.


Installation
~~~~~~~~~~~~

To install just run:

.. code:: shell

    $ pip3 install libgen.py


Usage
~~~~~

.. code:: shell

    $ libgen -h
    usage: libgen [-h] -s SEARCH [-n]

    Read more, kids.

    optional arguments:
      -h, --help            show this help message and exit
      -s SEARCH, --search SEARCH
                            search term
      -n, --non-interactive
                            non interactive mode, download first available choice


Dependencies
~~~~~~~~~~~~

Install all the dependencies with:

.. code:: bash

    $ pip3 install -r requirements.txt

License
~~~~~~~

Distributed under the MIT license. See LICENSE for details.

.. |PyPy Package| image:: https://badge.fury.io/py/libgen.py.svg
   :target: https://badge.fury.io/py/libgen.py
.. |Build Status| image:: https://travis-ci.org/adolfosilva/libgen.py.svg?branch=master
   :target: https://travis-ci.org/adolfosilva/libgen.py
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-orange.svg
   :target: https://opensource.org/licenses/MIT
