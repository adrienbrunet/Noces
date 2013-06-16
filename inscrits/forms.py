from django import forms
from django.forms import ModelForm
from .models import Inscrits


class InscritsForm(ModelForm):
    '''Form to submit the files.'''

    class Meta:
        model = Inscrits
