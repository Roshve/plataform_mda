# Generated by Django 3.1.2 on 2020-12-22 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201221_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_email', models.EmailField(blank=True, max_length=320)),
                ('leader_name', models.CharField(blank=True, max_length=100)),
                ('leader_lastname', models.CharField(blank=True, max_length=100)),
                ('cost_center', models.IntegerField()),
                ('product', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=100)),
                ('employee_lastname', models.CharField(blank=True, max_length=100)),
                ('management_consulting', models.CharField(blank=True, max_length=100)),
                ('employee_dni', models.IntegerField()),
                ('profile_equal', models.CharField(blank=True, max_length=100)),
                ('employee_replace', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.leader')),
            ],
        ),
        migrations.DeleteModel(
            name='new_user',
        ),
    ]
