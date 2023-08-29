from django import forms
from .models import Asset, AssetCategory
from django.utils import timezone

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description', 'purchase_date', 'category']
        
    def clean_purchase_date(self):
        purchase_date = self.cleaned_data['purchase_date']
        if purchase_date > timezone.now().date():
            raise forms.ValidationError("Purchase date cannot be in the future.")
        return purchase_date    

class AssetCategoryForm(forms.ModelForm):
    class Meta:
        model = AssetCategory
        fields = ['name', 'description']
