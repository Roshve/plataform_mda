# Generated by Django 3.1.2 on 2020-12-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_email', models.EmailField(blank=True, max_length=320)),
                ('leader_name', models.CharField(blank=True, max_length=100)),
                ('leader_lastname', models.CharField(blank=True, max_length=100)),
                ('cost_center', models.IntegerField(blank=True, max_length=3)),
                ('product', models.IntegerField(blank=True, max_length=8)),
                ('employee_name', models.CharField(blank=True, max_length=100)),
                ('employee_lastname', models.CharField(blank=True, max_length=100)),
                ('management_consulting', models.CharField(blank=True, max_length=100)),
                ('employee_dni', models.IntegerField(blank=True, max_length=12)),
                ('profile_equal', models.CharField(blank=True, max_length=100)),
                ('employee_replace', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]