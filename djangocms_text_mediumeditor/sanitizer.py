# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import bleach

from . import settings


def clean_html(text):
    """
    Strip disallowed HTML tags and attributes from given input. Allowed tags
    and attributes can be defined in settings.

    :param text: HTML to sanitize from disallowed tags and attributes.
    :type text: str

    :return: Clean version of given HTML where disallowed tags and attributes
             have been removed from.
    :rtype: str
    """
    return bleach.clean(
        text=text,
        tags=settings.TEXT_MEDIUMEDITOR_HTML_ALLOWED_TAGS,
        attributes=settings.TEXT_MEDIUMEDITOR_HTML_ALLOWED_ATTRIBUTES,
    )
