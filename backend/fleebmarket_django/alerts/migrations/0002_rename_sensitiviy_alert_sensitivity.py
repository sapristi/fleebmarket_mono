# Generated by Django 3.2.2 on 2021-08-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='sensitiviy',
            new_name='sensitivity',
        ),
    ]
