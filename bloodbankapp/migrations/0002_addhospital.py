# Generated by Django 2.2.5 on 2019-10-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addhospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(blank=True, max_length=400, null=True)),
                ('address', models.CharField(blank=True, max_length=400, null=True)),
                ('phone', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]