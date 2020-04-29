# Generated by Django 2.2.5 on 2019-10-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0003_bloodrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donate',
            old_name='date',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='donate',
            old_name='father_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='donate',
            old_name='hos',
            new_name='fathername',
        ),
        migrations.RenameField(
            model_name='donate',
            old_name='mobile',
            new_name='hospital',
        ),
        migrations.AddField(
            model_name='donate',
            name='phone',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
