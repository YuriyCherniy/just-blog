# Generated by Django 3.2.4 on 2021-07-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('post', models.ManyToManyField(to='posts.Post')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
