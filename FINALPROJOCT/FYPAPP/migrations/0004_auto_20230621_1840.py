# Generated by Django 2.2 on 2023-06-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0003_auto_20230621_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoice',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='questionlongterm',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='questionshortterm',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]