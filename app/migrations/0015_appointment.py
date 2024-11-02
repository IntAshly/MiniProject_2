# Generated by Django 5.1 on 2024-08-11 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_vaccinerequesthistory_approved_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('health_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.healthprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vaccine')),
            ],
        ),
    ]