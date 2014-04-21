from django.test import TestCase
from django.shortcuts import render
from django.forms.forms import BoundField

from authtools.forms import UserCreationForm

from tunes.templatetags.add_css import add_class_to_field

class TunesTemplateTagsTestCase(TestCase):

    def test_add_class_to_field(self):
        """
        Confirm we can add a class to a form field
        """
        form = UserCreationForm()
        field = BoundField(form, form.fields['email'], 'email')
        field_with_class = add_class_to_field(field, 'form-control')
        self.assertIn('form-control', field_with_class)

