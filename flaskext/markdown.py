# -*- coding: utf-8 -*-
"""
    flaskext.markdown
    ~~~~~~~~~~~~~~~~~

    Description of the module goes here...

    :copyright: (c) 2010 by Dan Colish.
    :license: BSD, MIT see LICENSE for more details.
"""
from __future__ import absolute_import
from flask import current_app
import markdown as md


def markdown(value):
    return md.markdown(value)


def load_markdown():
    current_app.jinja_env.filters.append(markdown)
