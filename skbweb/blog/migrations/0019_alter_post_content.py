# Generated by Django 3.2.7 on 2021-11-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', verbose_name='Контент'),
            preserve_default=False,
        ),
    ]
