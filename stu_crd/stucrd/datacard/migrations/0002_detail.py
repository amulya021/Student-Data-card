# Generated by Django 3.2 on 2021-11-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('qualif', models.CharField(max_length=200)),
            ],
        ),
    ]
