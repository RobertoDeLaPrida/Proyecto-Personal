# Generated by Django 4.2.9 on 2024-02-05 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
    ]
