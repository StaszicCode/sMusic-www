#!/usr/bin/python2
# -*- coding: utf-8 -*-

from distutils.core import setup
from smusicwww import __version__

setup(name="sMusicServer",
      version=__version__,
      description="Serwer sMusic",
      url="https://github.com/mRokita/sMusic-core/",
      author="Michał Rokita & Artur Puzio",
      author_email="mrokita@mrokita.pl & cytadela88@gmail.com",
      packages=["smusicwww"],
      scripts=["sMusicServer"],
      requires=["flask", "jinja2"],
      data_files=[('/etc/sMusic/', ['server.default.ini']),
                  ('/usr/share/sMusic/', ['smusicwww.wsgi']),
                  ('/usr/lib/systemd/system', ['sMusicServer.service'])],
      )
