# Generated by Django 3.1.7 on 2021-05-18 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_customuser_record_userotp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='warden_email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='warden_id',
        ),
    ]
