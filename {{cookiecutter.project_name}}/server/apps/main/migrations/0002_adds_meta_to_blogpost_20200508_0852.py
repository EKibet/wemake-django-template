# Generated by Django 2.2.12 on 2020-05-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'BlogPost', 'verbose_name_plural': 'BlogPosts'},
        ),
    ]