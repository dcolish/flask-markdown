# -*- coding: utf-8 -*-
"""
    flaskext.markdown
    ~~~~~~~~~~~~~~~~~

    Description of the module goes here...

    :copyright: (c) 2010 by Dan Colish.
    :license: BSD, MIT see LICENSE for more details.
"""
from __future__ import absolute_import
import jinja2
import jinja2.ext
import markdown
from flaskext.jinja2extender import extend_jinja


def load_markdown(app):
    extend_jinja(app, [MarkdownExtension])


class MarkdownExtension(jinja2.ext.Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdowner=markdown.Markdown(),
        )

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        body = parser.parse_statements(
            ['name:endmarkdown'],
            drop_needle=True,
        )
        return jinja2.nodes.CallBlock(
            self.call_method('_markdown_support'),
            [],
            [],
            body,
        ).set_lineno(lineno)

    def _markdown_support(self, caller):
        return self.environment.markdowner.convert(caller()).strip()
