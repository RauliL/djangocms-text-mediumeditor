# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


#: Whether HTML received from the editor should be sanitized or not.
TEXT_MEDIUMEDITOR_HTML_SANITIZE = getattr(
    settings,
    "TEXT_MEDIUMEDITOR_HTML_SANITIZE",
    True,
)

#: List of allowed HTML tags which are not sanitized. By default it's the list
#: of HTML tags supported by default Medium editor toolbar.
TEXT_MEDIUMEDITOR_HTML_ALLOWED_TAGS = getattr(
    settings,
    "TEXT_MEDIUMEDITOR_HTML_ALLOWED_TAGS",
    (
        "a",
        "b",
        "blockquote",
        "br",
        "h2",
        "h3",
        "i",
        "p",
        "u",
    ),
)

#: Dictionary which maps allowed HTML attributes to allowed HTML tags. By
#: default only "href" tag on link elements is allowed.
TEXT_MEDIUMEDITOR_HTML_ALLOWED_ATTRIBUTES = getattr(
    settings,
    "TEXT_MEDIUMEDITOR_HTML_ALLOWED_ATTRIBUTES",
    {
        "a": ("href",),
    },
)
