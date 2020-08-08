from django import forms
from .models import fpoproduct


class ProductForm(forms.ModelForm):
    productname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the productname...'
        }
    ))
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the description...'
        }
    ))
    quantity = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the quantity...'
        }
    ))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the price ...'
        }
    ))
    datefrom = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the starting date...'
        }
    ))
    dateto = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the end date...'
        }
    ))
    FPO = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the fpo registration ID...'
        }
    ))
    res=forms.FileField(widget=forms.FileInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Enter Profile Picture...'
            }
    ))
    
    class Meta:
        model = fpoproduct
        fields = ('quantity','description','FPO','res','productname','price','dateto','datefrom')
