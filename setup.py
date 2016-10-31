#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


INSTALL_REQUIRES = [
    "bleach>=1.4",
    "django-cms>=3.3.0",
]


setup(
    name="djangocms-text-mediumeditor",
    version="0.0.1",
    description="Text plugin for Django CMS which uses Medium editor",
    author="Rauli Laine",
    author_email="rauli.laine@iki.fi",
    url="https://github.com/RauliL/djangocms-text-mediumeditor",
    packages=[
        "djangocms_text_mediumeditor",
    ],
    install_requires=INSTALL_REQUIRES,
    platforms=["OS Independent"],
)
