# Generated by Django 3.0.6 on 2020-05-23 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('code', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtask', models.CharField(max_length=255, unique=True)),
                ('statut', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('date_debut', models.CharField(max_length=255, null=True)),
                ('date_fin', models.CharField(max_length=255, null=True)),
                ('idAgent', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='suppervision.Agent')),
            ],
        ),
    ]
