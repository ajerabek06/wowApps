# Generated by Django 3.1 on 2020-09-01 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mythicPlusScore', '0002_auto_20200901_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcharacterinfo',
            name='notes',
        ),
    ]
