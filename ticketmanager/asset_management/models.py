from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, AbstractUser

# Model for asset categories
class AssetCategory(models.Model):
    # The name of the asset category and description
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        # Returns the name of the asset category when it's converted to a string
        return self.name
    
class Meta:
        # Defines permissions for asset category management in the admin panel
        permissions = [
            ("can_view_assetcategory", "Can view asset category"),
            ("can_add_assetcategory", "Can add asset category"),
            ("can_change_assetcategory", "Can change asset category"),
            ("can_delete_assetcategory", "Can delete asset category"),
        ]
class Asset(models.Model):
    # The name of asset, description, purchase date and category
    name = models.CharField(max_length=200)
    description = models.TextField()
    purchase_date = models.DateField()
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)

    def __str__(self):
        # Returns the name of the asset when it's converted to a string
        return self.name
    
    class Meta:
        # Defines permissions for asset management in the admin panel
        permissions = [
            ("can_view_asset", "Can view asset"),
            ("can_add_asset", "Can add asset"),
            ("can_change_asset", "Can change asset"),
            ("can_delete_asset", "Can delete asset"),
        ]

class UserProfile(models.Model):
    # One-to-one relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username        

class CustomUser(AbstractUser):
    # An optional profile picture
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # A user's bio
    bio = models.TextField(null=True, blank=True)
    # User groups for access control
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
     # User-specific permissions
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username