# Generated by Django 3.2.6 on 2022-05-06 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='referece_number',
            field=models.CharField(default='2456', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='student_all_info',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myversity.registration'),
        ),
    ]
