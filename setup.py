from setuptools import setup


setup(
    name='Flask-Markdown',
    version='1',
    url='http://github.com/MorizMensi/flask-markdown',
    license='BSD',
    author='Dan Colish',
    author_email='dcolish@gmail.com',
    description='Small extension to make using markdown easy',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Markdown',
        ],
    classifiers=[
        'Development Status :: 5 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
