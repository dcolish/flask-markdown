from flask import Flask, render_template_string

from flaskext.markdown import Markdown


def run_client():
    app = Flask(__name__)
    app.debug = True
    md = Markdown(app)

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

    return app.test_client()


def test_render_inline():
    client = run_client()
    resp = client.open('/test_inline')
    assert resp.data == '<p>This is <em>markdown</em></p>'


def test_render_var_block():
    client = run_client()
    resp = client.open('/test_var_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'


def test_render_in_block():
    client = run_client()
    resp = client.open('/test_in_block')
    assert resp.data == '<p>This is a <em>markdown</em> block</p>'
