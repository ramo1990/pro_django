from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):

    class Meta:
        model = Cours 

        fields = [
            'nom',
            'description',
        ]
    
    #def clean_nom(self,*args, **kwargs):
    #    nom = self.cleaned_data.get("nom")
    #    if nom != "français":
    #        raise forms.ValidationError("Ce cours n'est pas autorisé")
    #    return nom