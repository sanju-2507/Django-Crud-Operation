# Generated by Django 4.0.1 on 2022-01-31 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('example', '0002_delete_course_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_enrolled', models.DateField()),
                ('final_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='example.Enrollment', to='example.Student'),
        ),
    ]