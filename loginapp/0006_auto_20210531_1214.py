# Generated by Django 3.1.7 on 2021-05-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_auto_20210518_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='student_email',
            field=models.EmailField(max_length=255),
        ),
    ]
