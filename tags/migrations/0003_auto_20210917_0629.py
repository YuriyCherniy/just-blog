# Generated by Django 3.2.4 on 2021-09-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=20, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
