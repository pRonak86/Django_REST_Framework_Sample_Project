# Generated by Django 3.0.1 on 2020-10-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=30)),
                ('StudentLastName', models.CharField(max_length=30)),
                ('StudentContact', models.BigIntegerField()),
            ],
        ),
    ]
