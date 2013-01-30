from flask import Flask, render_template_string
from nose.tools import with_setup

from flaskext.markdown import Extension, Markdown
from mdx_simple import SimpleExtension, SimplePreprocessor

app = Flask(__name__)
app.debug = True
autoescape_default = False
md = Markdown(app,
              autoescape=autoescape_default)

def setup():

    @app.route('/test_inline')
    def view_render_inline():
        mystr = u'This is *markdown*'
        return render_template_string('{{mystr|markdown}}', mystr=mystr)

    @app.route('/test_var_block')
    def view_render_var_block():
        mystr = u'This is a *markdown* block'
        template = '''{% filter markdown %}{{mystr}}{% endfilter %}'''
        return render_template_string(template, mystr=mystr)

    @app.route('/test_in_block')
    def view_render_in_block():
        tmp = u'{% filter markdown %}This is a *markdown* block{% endfilter %}'
        return render_template_string(tmp)

    @app.route('/test_register')
    def view_render_registered_extension():
        md.register_extension(SimpleExtension)

        text = """[[[
This is now a paragraph div
]]]"""
        return render_template_string(u"{{ text|markdown }}", text=text)

    @app.route('/test_extend')
    def view_render_decorated_extension():
        @md.extend()
        class SimpleExtension(Extension):
            def extendMarkdown(self, md, md_globals):
                md.preprocessors.add('prover_block',
                                     SimplePreprocessor(md),
                                     '_begin')
                md.registerExtension(self)

        text = """[[[
This is now a paragraph div
]]]"""
        return render_template_string(u"{{ text|markdown }}", text=text)

    @app.route('/test_autoescape_off')
    def view_render_autoescape_off():
        mystr = u'This is a <b>markdown</b> block'
        result = render_template_string(('{% autoescape false %}'
                                         '{{mystr|markdown}}'
                                         '{% endautoescape %}'), mystr=mystr)
        return result

    @app.route('/test_autoescape_on')
    def view_render_autoescape_on():
        mystr = u'This is a <b>markdown</b> block'
        result = render_template_string(('{% autoescape true %}'
                                         '{{mystr|markdown}}'
                                         '{% endautoescape %}'), mystr=mystr)
        return result


def inject_autoescape_true():
    app.config['markdown_autoescape'] = True


def inject_autoescape_false():
    app.config['markdown_autoescape'] = False


def inject_autoescape_default():
    app.config['markdown_autoescape'] = autoescape_default


def test_render_inline():
    resp = app.test_client().open('/test_inline')
    assert resp.data == '<p>This is <em>markdown</em></p>'


def test_render_var_block():
    resp = app.test_client().open('/test_var_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'


def test_render_in_block():
    resp = app.test_client().open('/test_in_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'


def test_render_register_extension():
    resp = app.test_client().open('/test_register')
    assert resp.data == "<div><p>This is now a paragraph div</p></div>"


def test_render_extend_decorator():
    resp = app.test_client().open('/test_extend')
    assert resp.data == "<div><p>This is now a paragraph div</p></div>"


@with_setup(inject_autoescape_true, inject_autoescape_default)
def test_render_autoescape_off_obey():
    resp = app.test_client().open('/test_autoescape_off')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"


@with_setup(inject_autoescape_true, inject_autoescape_default)
def test_render_autoescape_on_obey():
    resp = app.test_client().open('/test_autoescape_on')
    assert resp.data == "<p>This is a &lt;b&gt;markdown&lt;/b&gt; block</p>"


@with_setup(inject_autoescape_false, inject_autoescape_default)
def test_render_autoescape_off_ignore():
    resp = app.test_client().open('/test_autoescape_off')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"


@with_setup(inject_autoescape_false, inject_autoescape_default)
def test_render_autoescape_on_ignore():
    resp = app.test_client().open('/test_autoescape_on')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"
