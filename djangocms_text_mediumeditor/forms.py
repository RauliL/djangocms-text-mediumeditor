# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from .models import MediumEditorText
from .widgets import MediumEditorWidget


class MediumEditorTextForm(forms.ModelForm):
    body = forms.CharField(
        widget=MediumEditorWidget,
        required=False,
    )

    class Meta:
        model = MediumEditorText
        fields = ("body",)
