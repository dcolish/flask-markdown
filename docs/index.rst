Welcome to Flask Markdown's documentation!
==========================================

.. module:: flaskext.markdown


Flask-Markdown adds support for `Markdown`_ to your `Flask`_
application.  There is little to no documentation for it, but 
it works just the same as markdown would normally.

All source code can be found at `Github`_


Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Markdown

or alternatively if you have pip installed::

    $ pip install Flask-Markdown

How to Use
----------

To use you must construct a :class:`Markdown` with your :class:`~flask.Flask` instance.

::

       from flaskext.markdown import Markdown
       Markdown(app)

Then in your template
::

        {% filter markdown %}
        Your Markdown
        =============
        {% endfilter %}

You can also do
::

        {{ mkd|markdown }}


Optionally, you can keep a reference to the Markdown instance and use that
to register custom extensions by calling :func:`Markdown.register_extension` or
decorating the extension class with :func:`Markdown.extend`

API Reference
-------------

.. autoclass:: Markdown
   :members:

.. _`Flask`: http://flask.pocoo.org/
.. _`Markdown`: http://www.freewisdom.org/projects/python-markdown/
.. _`Github`: http://www.github.com/dcolish/flask-markdown
