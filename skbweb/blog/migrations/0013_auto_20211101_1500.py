# Generated by Django 3.2.7 on 2021-11-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover2',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Документы'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover3',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Документы'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover4',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Документы'),
        ),
    ]