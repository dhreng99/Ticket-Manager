from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class AssetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Meta:
        permissions = [
            ("can_view_assetcategory", "Can view asset category"),
            ("can_add_assetcategory", "Can add asset category"),
            ("can_change_assetcategory", "Can change asset category"),
            ("can_delete_assetcategory", "Can delete asset category"),
        ]
class Asset(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    purchase_date = models.DateField()
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ("can_view_asset", "Can view asset"),
            ("can_add_asset", "Can add asset"),
            ("can_change_asset", "Can change asset"),
            ("can_delete_asset", "Can delete asset"),
        ]
