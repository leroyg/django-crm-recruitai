# Generated by Django 3.1.4 on 2022-04-26 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20220426_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='last_name',
            new_name='lastname',
        ),
    ]