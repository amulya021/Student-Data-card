# Generated by Django 3.2 on 2021-12-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacard', '0015_auto_20211112_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=200)),
                ('enam', models.CharField(max_length=200)),
            ],
        ),
    ]
