# Generated by Django 5.1.2 on 2024-10-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_amt',
            field=models.FloatField(max_length=50, null=True),
        ),
    ]