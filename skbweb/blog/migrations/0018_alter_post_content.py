# Generated by Django 3.2.7 on 2021-11-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20211103_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Документ-1'),
        ),
    ]
