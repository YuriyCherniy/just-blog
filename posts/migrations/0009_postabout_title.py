# Generated by Django 3.2.4 on 2021-09-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210901_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='postabout',
            name='title',
            field=models.CharField(default='oiuyt', max_length=200, verbose_name='название'),
            preserve_default=False,
        ),
    ]
