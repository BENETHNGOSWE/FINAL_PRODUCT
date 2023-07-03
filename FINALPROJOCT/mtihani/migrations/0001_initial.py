# Generated by Django 2.2 on 2023-05-23 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FYPAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MtihaniTaarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(blank=True, max_length=100, null=True)),
                ('semeter', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SavedExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtihani', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mtihani',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulecode', models.CharField(blank=True, max_length=50, null=True)),
                ('semeter', models.CharField(blank=True, max_length=50, null=True)),
                ('exam_name', models.CharField(max_length=50)),
                ('examdate', models.DateField(null=True)),
                ('examtime', models.CharField(blank=True, max_length=50, null=True)),
                ('examinationDescription', models.CharField(blank=True, max_length=300, null=True)),
                ('examinationDescription2', models.CharField(blank=True, max_length=300, null=True)),
                ('examinationDescription3', models.CharField(blank=True, max_length=300, null=True)),
                ('num_questions', models.IntegerField()),
                ('num_shortquestions', models.IntegerField()),
                ('num_longquestions', models.IntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Course')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinationType', models.CharField(blank=True, max_length=30, null=True)),
                ('examinationName', models.CharField(blank=True, max_length=30, null=True)),
                ('semeter', models.IntegerField(blank=True, null=True)),
                ('examDuration', models.TimeField(blank=True, null=True)),
                ('examFullmark', models.IntegerField(blank=True, null=True)),
                ('examinationDescription', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Course')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
                ('questionChoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.QuestionShortterm')),
                ('questionLong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.QuestionLongTerm')),
                ('questionSection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.QuestionSection')),
            ],
        ),
    ]
