from django.db import models

class AssetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    purchase_date = models.DateField()
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
