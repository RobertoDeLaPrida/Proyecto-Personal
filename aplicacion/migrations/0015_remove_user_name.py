# Generated by Django 4.2.10 on 2024-02-14 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
