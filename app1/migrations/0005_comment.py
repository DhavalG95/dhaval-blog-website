# Generated by Django 4.1.4 on 2022-12-26 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_form_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Content', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app1.form')),
            ],
        ),
    ]
