# Flask-Markdown

This is a small module to load markdown processing into
your flask.

## To setup the development environment

```bash
$ git clone https://github.com/dcolish/flask-markdown.git
$ virtualenv ENV
$ . ENV/bin/activate
$ python setup.py develop
```

## Run the test site

```bash
$ python setup.py test
```

#### !! There is a bug in the current release of 'nose' which results in 'NoneType' objects being called on test-suite shutdown. Please ignore this.

## To setup the documentation environment

```bash
$ pip install sphinx
$ git submodule init
$ git submodule update
```
