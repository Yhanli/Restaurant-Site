# Generated by Django 2.2.10 on 2020-03-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_mainpage_logoimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
