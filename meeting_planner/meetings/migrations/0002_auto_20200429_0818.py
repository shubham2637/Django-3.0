# Generated by Django 3.0.5 on 2020-04-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
