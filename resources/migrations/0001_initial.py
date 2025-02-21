# Generated by Django 4.0.3 on 2022-03-20 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceTimeZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_time_zone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resource')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resource')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.skill')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceSkillLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resourceskills')),
                ('skill_level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.skilllevel')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_hour', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resource')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('hours_per_day', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resource')),
            ],
        ),
    ]
