# Generated by Django 3.1 on 2020-11-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlogdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usr_table',
            old_name='Password',
            new_name='password',
        ),
        migrations.AddField(
            model_name='usr_table',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='usr_table',
            name='UserName',
            field=models.TextField(null=True, unique=True),
        ),
    ]
