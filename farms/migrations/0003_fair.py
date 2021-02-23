# Generated by Django 3.1.4 on 2021-02-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_auto_20210114_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('when', models.CharField(max_length=100)),
                ('periodical', models.BooleanField(default=True)),
                ('organizer', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.address')),
                ('farms', models.ManyToManyField(to='farms.Farm')),
            ],
        ),
    ]
