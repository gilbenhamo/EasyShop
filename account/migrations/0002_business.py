# Generated by Django 3.1.3 on 2020-12-02 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.user')),
                ('business_name', models.CharField(max_length=50)),
                ('business_address', models.CharField(max_length=50)),
                ('business_phone', models.CharField(max_length=10)),
                ('business_info', models.TextField(max_length=255)),
                ('business_category', models.CharField(max_length=50)),
            ],
        ),
    ]
