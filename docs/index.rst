Welcome to Flask Markdown's documentation!
==========================================

Flask-Markdown adds support for `Markdown`_ to your `Flask`_
application.  There is little to no documentation for it, but 
it works just the same as markdown would normally.


Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Markdown

or alternatively if you have pip installed::

    $ pip install Flask-Markdown

How to Use
----------

    To use::
       from flaskext.markdown import Markdown
       md = Markdown(app)

    Then in your template::
        {% filter markdown %}
        Your Markdown
        =============
        {% endfilter %}

    You can also do::
        {{ mymarkdown | markdown}}

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

