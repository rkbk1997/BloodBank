# Generated by Django 2.2.5 on 2019-10-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0002_addhospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('fathername', models.CharField(blank=True, max_length=400, null=True)),
                ('group', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.CharField(blank=True, max_length=400, null=True)),
                ('phone', models.CharField(blank=True, max_length=400, null=True)),
                ('address', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
