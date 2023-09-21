from django.contrib import admin
from .models import Asset, AssetCategory, UserProfile

# Register the AssetCategory model with the admin site.
admin.site.register(AssetCategory)

# Register the Asset model with the admin site.
admin.site.register(Asset)

# Register the UserProfile model with the admin site.
admin.site.register(UserProfile)