from flask import Flask, render_template_string

from flaskext.markdown import Markdown
mystr = u'This is *markdown*'

def run_client():
    app = Flask(__name__)
    app.debug = True
    md = Markdown(app)

    @app.route('/test_render')
    def view_markdown_render():

        return render_template_string('{{mystr|markdown}}', mystr=mystr)

    return app.test_client()


def test_render_markdown():
    client = run_client()
    resp = client.open('/test_render')
    assert resp.data == '<p>This is <em>markdown</em></p>'
