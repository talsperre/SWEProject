# Generated by Django 3.0.5 on 2020-04-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarize', '0003_auto_20200414_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='VideoPath',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]