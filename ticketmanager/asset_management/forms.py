from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Asset, AssetCategory, CustomUser
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

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio')  
        
class AssetUpdateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description', 'purchase_date']
                