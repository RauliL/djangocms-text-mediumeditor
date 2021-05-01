#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


INSTALL_REQUIRES = [
    "bleach>=1.4",
    "django-cms>=3.3.0",
]


setup(
    name="djangocms-text-mediumeditor",
    version="0.2.0",
    description="Text plugin for Django CMS which uses Medium editor",
    author="Rauli Laine",
    author_email="rauli.laine@iki.fi",
    url="https://github.com/RauliL/djangocms-text-mediumeditor",
    packages=[
        "djangocms_text_mediumeditor",
        "djangocms_text_mediumeditor.migrations",
    ],
    install_requires=INSTALL_REQUIRES,
    license="LICENSE",
    platforms=["OS Independent"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
