# Generated by Django 2.2 on 2023-05-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoice',
            name='answer',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionlongterm',
            name='answer',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionshortterm',
            name='answer',
            field=models.TextField(max_length=200),
        ),
    ]