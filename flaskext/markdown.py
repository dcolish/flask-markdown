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
from flask import current_app, Markup
import markdown2 as md2


class Markdown(md2.Markdown):

    def __init__(self, app, *args, **kw):
        super(Markdown, self).__init__(*args, **kw)
        app.jinja_env.filters.update({'markdown': self.__call__})

    def __call__(self, stream):
        if hasattr(current_app, 'genshi_instance'):
            return self.convert(stream)
        else:
            return Markup(self.convert(stream))
