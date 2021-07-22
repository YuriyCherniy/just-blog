# Generated by Django 3.2.4 on 2021-07-13 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='postabout',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]