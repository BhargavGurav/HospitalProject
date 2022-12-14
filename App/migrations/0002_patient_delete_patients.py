# Generated by Django 4.0.3 on 2022-08-12 10:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Trans')], max_length=7)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Patients',
        ),
    ]
