# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.forms.widgets import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class MediumEditorWidget(Textarea):

    def __init__(self, attrs=None):
        super(Textarea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if attrs and "id" in attrs:
            editor_id = attrs["id"]
        else:
            if not attrs:
                attrs = {}
            attrs["id"] = "mediumeditor_%s" % (uuid.uuid4(),)

        context = {"editor_id": editor_id}

        return (
            super(MediumEditorWidget, self).render(name, value, attrs)
            + mark_safe(render_to_string("cms/plugins/widgets/mediumeditor.html", context))
        )
