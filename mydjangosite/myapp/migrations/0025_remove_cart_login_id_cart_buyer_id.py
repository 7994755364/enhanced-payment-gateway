# Generated by Django 4.2.14 on 2024-10-07 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_remove_cart_buyer_id_cart_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='LOGIN_ID',
        ),
        migrations.AddField(
            model_name='cart',
            name='Buyer_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.buyer'),
            preserve_default=False,
        ),
    ]