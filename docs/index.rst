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

When initializing your applicattion run::

from flaskext.markdown import load_markdown
app = Flask(__name__)
load_markdown(app)

Your template can then process any markdown using::

{% markdown %}
{{ lesson.text }}
{% endmarkdown %}


Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

