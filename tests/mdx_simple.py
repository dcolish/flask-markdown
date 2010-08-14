"""
Simple Extension for Python-Markdown
=============================================

A simple example:

  [[[
  This is now a paragraph div
  ]]]
"""
from cgi import escape
import re
import markdown


class SimpleExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('prover_block',
                             SimplePreprocessor(md),
                             '_begin')
        md.registerExtension(self)


class SimplePreprocessor(markdown.preprocessors.Preprocessor):

    RE = re.compile(r'(?P<begin>^\[{3,})[ ]*\n(?P<content>.*?)'
                    '(?P<end>^\]{3,})[ ]*$',
                    re.MULTILINE | re.DOTALL)
    WRAP = """<div><p>{0}</p></div>"""

    def __init__(self, md):
        markdown.preprocessors.Preprocessor.__init__(self, md)

    def run(self, lines):
        text = "\n".join(lines)
        while 1:
            m = self.RE.search(text)
            if m:
                content = m.group('content').strip()
                output = self.WRAP.format(escape(content, quote=True))
                placeholder = self.markdown.htmlStash.store(output,
                                                            safe=True)
                text = '%s\n%s\n%s' % (text[:m.start()], placeholder,
                                      text[m.end():])
            else:
                break
        return text.split("\n")
