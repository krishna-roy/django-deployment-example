# Generated by Django 3.2.5 on 2021-07-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
