# Generated by Django 2.0.5 on 2021-02-06 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fn_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
