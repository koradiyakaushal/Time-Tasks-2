# Generated by Django 3.1.2 on 2020-11-04 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
