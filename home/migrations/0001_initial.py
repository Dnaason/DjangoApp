# Generated by Django 2.2.12 on 2022-10-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=45)),
                ('Lname', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
    ]
