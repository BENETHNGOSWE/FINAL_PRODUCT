# Generated by Django 2.2 on 2023-06-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0004_auto_20230621_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoice',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionlongterm',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionshortterm',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]