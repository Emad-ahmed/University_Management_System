# Generated by Django 3.2.6 on 2022-05-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myversity', '0004_auto_20220522_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('postion', models.CharField(max_length=250)),
                ('department', models.CharField(choices=[('CSE', 'Department of CSE'), ('BBA', 'Department of Business Administration'), ('Law', 'Department of Law'), ('Architecture', 'Department of Architecture'), ('EEE', 'Department of EEE'), ('English', 'Department of English'), ('Civil', 'Department of Civil Engineering')], default='CSE', max_length=50)),
                ('cell_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField()),
                ('area_of_study', models.TextField()),
                ('eventsimg', models.ImageField(upload_to='eventsimages/')),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='referece_number',
            field=models.CharField(default='6804', max_length=7, unique=True),
        ),
    ]