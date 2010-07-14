# -*- coding: utf-8 -*-
"""
    flaskext.markdown
    ~~~~~~~~~~~~~~~~~

    Markdown filter class for Flask
    To use::
       from flaskext.markdown import Markdown
       # reconfigure app jinja enviroment
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

    def __init__(self, app, *args, **kw):
        # markdown still uses old style classes
        self._instance = md.Markdown(*args, **kw)
        app.jinja_env.filters.setdefault('markdown', self)

    def __call__(self, stream):
        return Markup(self._instance.convert(stream))
