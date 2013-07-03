from django import forms
from django.forms import ModelForm
from inscrits.models import Inscrits
from inscrits.models import Transport


class InscritsForm(ModelForm):
    '''Form to submit the files.'''

    class Meta:
        model = Inscrits

class TransportForm(ModelForm):
    '''Form to submit the transport needs'''

    Nom     = forms.CharField(label=(u'Nom'))
    Nombre  = forms.IntegerField(label=(u'Nombre de personnes'),required=False)
    Ville   = forms.CharField(label=(u'Ville/Gare/Aeroport de depart'),required=False)
    Date    = forms.CharField(label=(u'Date et heure approximative, ex: "Samedi matin"'),required=False)
    Contact = forms.CharField(label=(u'Contact pour vous joindre (tel ou mail) mettez un espace avant et apres le symbole @ et ecrivez "at" ou "arobase" a la place de @ pour eviter le spam..'),required=False)
    Remarque= forms.CharField(label=(u'Remarques'),required=False)

    class Meta:
        model = Transport
