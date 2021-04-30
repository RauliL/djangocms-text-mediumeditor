# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import MediumEditorTextForm
from .models import MediumEditorText


class MediumEditorTextPlugin(CMSPluginBase):
    model = MediumEditorText
    form = MediumEditorTextForm
    name = _("Text")
    render_template = "cms/plugins/mediumeditor_text.html"
    change_form_template = "cms/plugins/mediumeditor_text_change_form.html"

    def render(self, context, instance, placeholder):
        context.update({
            "body": instance.body,
            "placeholder": placeholder,
            "object": instance,
            "editor_id": "mediumeditor_%s" % uuid.uuid4(),
        })
        return context


plugin_pool.register_plugin(MediumEditorTextPlugin)
