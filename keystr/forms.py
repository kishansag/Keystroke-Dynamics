from django import forms

from .models import stroke

class StrokeForm(forms.ModelForm):

    class Meta:
        model = stroke
        fields = ('timecsv', 'keycsv','spincsv', 'email')

