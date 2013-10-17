#!/usr/bin/env python
from setuptools import setup

requires = ['feedgenerator >= 1.6', 'jinja2 >= 2.7', 'pygments', 'docutils',
            'pytz >= 0a', 'blinker', 'unidecode', 'six']

entry_points = {
    'console_scripts': [
        'pelican = pelican:main',
        'pelican-import = pelican.tools.pelican_import:main',
        'pelican-quickstart = pelican.tools.pelican_quickstart:main',
        'pelican-themes = pelican.tools.pelican_themes:main'
    ]
}


README = open('README.rst').read()
CHANGELOG = open('docs/changelog.rst').read()


setup(
    name="pelican",
    version="3.3",
    url='http://getpelican.com/',
    author='Alexis Metaireau',
    author_email='authors@getpelican.com',
    description="A tool to generate a static blog from reStructuredText or "
                "Markdown input files.",
    long_description=README + '\n' + CHANGELOG,
    packages=['pelican', 'pelican.tools'],
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
         'Environment :: Console',
         'License :: OSI Approved :: GNU Affero General Public License v3',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.3',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='pelican.tests',
)
