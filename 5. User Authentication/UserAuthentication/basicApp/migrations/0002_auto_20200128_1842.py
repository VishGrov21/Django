# Generated by Django 2.2.6 on 2020-01-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='appUser',
            new_name='user',
        ),
    ]