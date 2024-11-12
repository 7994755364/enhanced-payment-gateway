# Generated by Django 4.2.14 on 2024-10-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_cart_total_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=50, null=True)),
                ('cardholder_name', models.CharField(max_length=50, null=True)),
                ('expiration', models.CharField(max_length=50, null=True)),
                ('cvv', models.CharField(max_length=50, null=True)),
                ('balance', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]