# Generated by Django 4.0.5 on 2022-06-12 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0012_alter_registration_referece_number'),
        ('teacherapp', '0002_courseassign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('select_grade', models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='A', max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.deparetment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myversity.loginsite')),
            ],
        ),
    ]