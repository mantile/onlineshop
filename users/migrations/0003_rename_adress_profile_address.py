# Generated by Django 5.1.1 on 2024-09-24 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_first_name_profile_user_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adress',
            new_name='address',
        ),
    ]
