# Generated by Django 5.1.1 on 2024-10-10 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_mentalhealthdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentalhealthdetails',
            name='description',
        ),
        migrations.AlterField(
            model_name='mentalhealthdetails',
            name='age',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='MentalHealthDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('mental_health_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='app.mentalhealthdetails')),
            ],
        ),
    ]