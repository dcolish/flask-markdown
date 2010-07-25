# -*- coding: utf-8 -*-
"""
flaskext.markdown
~~~~~~~~~~~~~~~~~

Markdown filter class for Flask
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

:copyright: (c) 2010 by Dan Colish.
:license: BSD, MIT see LICENSE for more details.
"""
from __future__ import absolute_import
from flask import Markup
import markdown as md


class Markdown(object):
    """
    Simple wrapper class for Markdown objects, any options that are available
    for markdown may be passed as keyword arguments like so::

      md = Markdown(app,
                    extensions=['footnotes'],
                    extension_configs={'footnotes': ('PLACE_MARKER','~~~~~~~~')},
                    safe_mode=True,
                    output_format='html4',
                    )
    """

    def __init__(self, app, **markdown_options):
        """Markdown uses old style classes"""
        self._instance = md.Markdown(**markdown_options)
        app.jinja_env.filters.setdefault('markdown', self)

    def __call__(self, stream):
        return Markup(self._instance.convert(stream))
