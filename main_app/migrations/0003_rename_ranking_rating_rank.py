# Generated by Django 4.2.7 on 2023-11-05 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='ranking',
            new_name='rank',
        ),
    ]
