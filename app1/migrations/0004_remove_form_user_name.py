# Generated by Django 4.1.4 on 2022-12-24 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_form_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='user_name',
        ),
    ]
