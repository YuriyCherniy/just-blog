# Generated by Django 3.2.4 on 2021-09-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
    ]
