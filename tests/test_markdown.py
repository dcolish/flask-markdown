from functools import wraps

from flask import Flask, render_template_string

from flaskext.markdown import Extension, Markdown
from mdx_simple import SimpleExtension, SimplePreprocessor


class Fixture(object):

    def inject(self, auto_escape=False):
        def create_app(fn):
            @wraps(fn)
            def wrapper(*arg, **args):
                app = Flask(__name__)
                app.debug = True
                md = Markdown(app, auto_escape=auto_escape)

                @app.route('/test_inline')
                def view_render_inline():
                    mystr = u'This is *markdown*'
                    return render_template_string(
                        '{{mystr|markdown}}', mystr=mystr)

                @app.route('/test_var_block')
                def view_render_var_block():
                    mystr = u'This is a *markdown* block'
                    template = '''\
{% filter markdown %}{{mystr}}{% endfilter %}'''
                    return render_template_string(template, mystr=mystr)

                @app.route('/test_in_block')
                def view_render_in_block():
                    tmp = \
    u'{% filter markdown %}This is a *markdown* block{% endfilter %}'
                    return render_template_string(tmp)

                @app.route('/test_register')
                def view_render_registered_extension():
                    md.register_extension(SimpleExtension)

                    text = """[[[
This is now a paragraph div
]]]"""
                    return render_template_string(
                        u"{{ text|markdown }}", text=text)

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
                    return render_template_string(
                        u"{{ text|markdown }}", text=text)

                @app.route('/test_autoescape_off')
                def view_render_autoescape_off():
                    mystr = u'This is a <b>markdown</b> block'
                    result = render_template_string(
                        ('{% autoescape false %}'
                         '{{mystr|markdown}}'
                         '{% endautoescape %}'), mystr=mystr)
                    return result

                @app.route('/test_autoescape_on')
                def view_render_autoescape_on():
                    mystr = u'This is a <b>markdown</b> block'
                    result = render_template_string(
                        ('{% autoescape true %}'
                         '{{mystr|markdown}}'
                         '{% endautoescape %}'), mystr=mystr)
                    return result

                return fn(app, *args, **args)
            return wrapper
        return create_app

fixture = Fixture()


@fixture.inject()
def test_render_inline(app):
    resp = app.test_client().open('/test_inline')
    assert resp.data == '<p>This is <em>markdown</em></p>'


@fixture.inject()
def test_render_var_block(app):
    resp = app.test_client().open('/test_var_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'


@fixture.inject()
def test_render_in_block(app):
    resp = app.test_client().open('/test_in_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'


@fixture.inject()
def test_render_register_extension(app):
    resp = app.test_client().open('/test_register')
    assert resp.data == "<div><p>This is now a paragraph div</p></div>"


@fixture.inject()
def test_render_extend_decorator(app):
    resp = app.test_client().open('/test_extend')
    assert resp.data == "<div><p>This is now a paragraph div</p></div>"


@fixture.inject(auto_escape=False)
def test_render_autoescape_off_obey(app):
    resp = app.test_client().open('/test_autoescape_off')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"


@fixture.inject(auto_escape=True)
def test_render_autoescape_on_obey(app):
    resp = app.test_client().open('/test_autoescape_on')
    assert resp.data == "<p>This is a &lt;b&gt;markdown&lt;/b&gt; block</p>"


@fixture.inject(auto_escape=False)
def test_render_autoescape_off_ignore(app):
    resp = app.test_client().open('/test_autoescape_off')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"


@fixture.inject(auto_escape=False)
def test_render_autoescape_on_ignore(app):
    resp = app.test_client().open('/test_autoescape_on')
    assert resp.data == "<p>This is a <b>markdown</b> block</p>"
