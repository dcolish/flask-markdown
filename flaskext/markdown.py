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
from inspect import getmodule
import markdown as md


class Markdown(object):
    """
    Simple wrapper class for Markdown objects, any options that are available
    for markdown may be passed as keyword arguments like so::

      Markdown(app,
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

    def makeExtension(self, configs={}):
        """
        You must either force the decorated class to be imported
        or define it in the same file you instanciate Markdown
        """
        def decorator(ext_cls):
            return self.registerExtension(ext_cls, configs)
        return decorator

    def registerExtension(self, ext_cls, configs=None):
        """This will register an extension class with self._instance"""
        instance = ext_cls()
        self._instance.registerExtensions([instance], configs)
        module = getmodule(ext_cls)
        module.makeExtension = ext_cls
        return ext_cls
