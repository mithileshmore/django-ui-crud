# Generated by Django 3.0 on 2019-12-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('emp_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
