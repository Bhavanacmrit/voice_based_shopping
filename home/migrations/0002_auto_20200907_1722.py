# Generated by Django 3.1 on 2020-09-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.TextField()),
                ('ram', models.TextField()),
                ('hdd', models.TextField()),
                ('sdd', models.TextField()),
                ('display', models.TextField()),
                ('graphics', models.TextField()),
                ('battery', models.TextField()),
                ('rating', models.IntegerField()),
                ('highlights', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('color_variant', models.CharField(max_length=100)),
                ('memory_variant', models.TextField()),
                ('sim_type', models.CharField(max_length=50)),
                ('battery', models.TextField()),
                ('processor', models.TextField(max_length=50)),
                ('ram', models.TextField()),
                ('front_camera', models.TextField()),
                ('rear_camera', models.TextField()),
                ('resolution', models.TextField()),
                ('rating', models.IntegerField()),
                ('highlights', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='features',
        ),
    ]
