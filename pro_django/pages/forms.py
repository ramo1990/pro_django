from django import forms
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'active', 'live']

def clean_nom(self, *args, **kwargs):
    nom = self.cleaned_data.get('nom')
    if nom != 'ramoni':
        raise forms.ValidationError("le nom doit etre ramoni")
    return nom

def clean_description(self, *args, **kwargs):
    description = self.cleaned_data.get('description')
    if description != 'ramoni':
        raise forms.ValidationError("description doit etre ramoni")
    return description

class PureProduitForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class':'name',
        'placeholder':'Entrer le nom  du produit'
        }))
    description = forms.CharField(required=False,widget=forms.Textarea(
                attrs={
                    'rows':10,
                    'cols':60,
                    'class':'desc',
                    'id':'description'
                }), initial= 'description du  produit')
    prix = forms.FloatField(label='prix du produit')
    active = forms.BooleanField(help_text='Ce champs permet de savoir si le produit est active ou non')