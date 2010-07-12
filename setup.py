"""
Flask-Markdown
--------------

This is a small module to load markdown processing into
your flask.

Links
`````

* `documentation <http://packages.python.org/Flask-Markdown>`_
* `development version
  <http://github.com/dcolish/flask-markdown/zipball/master#egg=Flask-Markdown-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-Markdown',
    version='dev',
    url='http://github.com/dcolish/flask-markdown',
    license='BSD',
    author='Dan Colish',
    author_email='dcolish@gmail.com',
    description='Small extension to make using markup easy',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask-jinja2extender',
        'markdown',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
