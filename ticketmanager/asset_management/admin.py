from django.contrib import admin
from .models import Asset, AssetCategory, UserProfile

admin.site.register(AssetCategory)
admin.site.register(Asset)
admin.site.register(UserProfile)