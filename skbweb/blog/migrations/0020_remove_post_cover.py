# Generated by Django 3.2.7 on 2021-11-04 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
    ]
