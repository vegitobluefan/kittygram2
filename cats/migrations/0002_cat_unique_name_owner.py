# Generated by Django 3.2.3 on 2024-07-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cat',
            constraint=models.UniqueConstraint(fields=('name', 'owner'), name='unique_name_owner'),
        ),
    ]
