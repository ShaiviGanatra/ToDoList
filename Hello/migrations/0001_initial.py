# Generated by Django 2.1.5 on 2019-03-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('incharge', models.CharField(max_length=100)),
                ('submission_date', models.DateField()),
            ],
        ),
    ]
