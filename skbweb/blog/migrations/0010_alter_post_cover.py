# Generated by Django 3.2.7 on 2021-11-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Документы'),
        ),
    ]
