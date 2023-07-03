# Generated by Django 2.2 on 2023-05-23 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=30)),
                ('courseCode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Masomo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=30)),
                ('moduleCode', models.CharField(max_length=30)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Course')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionsection', models.CharField(choices=[('YES', 'YES'), ('NO', ' NO')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questiontype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicNumber', models.IntegerField()),
                ('topicName', models.CharField(max_length=30)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionShortterm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
                ('answer', models.TextField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Category')),
                ('somo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionLongTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Category')),
                ('somo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
                ('option1', models.TextField(max_length=100)),
                ('option2', models.TextField(max_length=100)),
                ('option3', models.TextField(max_length=100)),
                ('option4', models.TextField(max_length=100)),
                ('answer', models.TextField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Category')),
                ('somo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Masomo')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.Topic')),
            ],
        ),
    ]
