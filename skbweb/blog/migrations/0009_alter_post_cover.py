# Generated by Django 3.2.7 on 2021-11-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20211101_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Документы'),
        ),
    ]