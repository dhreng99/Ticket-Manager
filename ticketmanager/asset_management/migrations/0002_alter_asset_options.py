# Generated by Django 4.2.3 on 2023-08-25 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'permissions': [('can_view_asset', 'Can view asset'), ('can_add_asset', 'Can add asset'), ('can_change_asset', 'Can change asset'), ('can_delete_asset', 'Can delete asset')]},
        ),
    ]
