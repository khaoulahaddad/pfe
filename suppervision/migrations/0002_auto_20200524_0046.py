# Generated by Django 3.0.6 on 2020-05-23 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppervision', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='idAgent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppervision.Agent'),
        ),
    ]
