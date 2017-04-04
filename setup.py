from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='cs.portlet.calendar',
      version=version,
      description="Calendar portlet using fullcalendar.io",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='https://github.com/codesyntax/cs.portlet.calendar',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs', 'cs.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.api'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
