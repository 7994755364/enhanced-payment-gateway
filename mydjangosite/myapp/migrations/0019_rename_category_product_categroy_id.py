# Generated by Django 4.2.14 on 2024-09-26 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_product_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='CATEGROY_ID',
        ),
    ]
