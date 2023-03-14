# Generated by Django 4.1.7 on 2023-03-14 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FYPAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinationType', models.CharField(max_length=30)),
                ('examinationName', models.CharField(max_length=30)),
                ('semeter', models.IntegerField()),
                ('examDuration', models.TimeField()),
                ('examFullmark', models.IntegerField()),
                ('examinationDescription', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.masomo')),
                ('questionSection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.questionsection')),
            ],
        ),
    ]
