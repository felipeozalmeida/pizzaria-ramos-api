# Generated by Django 2.2.6 on 2019-10-19 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191019_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='imageUrl',
            new_name='image_file',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='imageAlt',
            new_name='image_text',
        ),
    ]
