# Generated by Django 4.2.14 on 2024-08-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_login_rename_cat_name_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
