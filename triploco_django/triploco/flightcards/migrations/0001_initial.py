# Generated by Django 5.0.7 on 2024-08-16 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_date', models.DateField()),
                ('flight_status', models.CharField(max_length=50)),
                ('airline_name', models.CharField(max_length=255)),
                ('airline_iata', models.CharField(max_length=50)),
                ('airline_icao', models.CharField(max_length=40)),
                ('flight_number', models.CharField(max_length=20)),
                ('flight_iata', models.CharField(max_length=20)),
                ('flight_icao', models.CharField(max_length=20)),
                ('departure_airport', models.CharField(max_length=255)),
                ('departure_airport_code', models.CharField(max_length=20)),
                ('departure_scheduled', models.DateTimeField()),
                ('departure_estimated', models.DateTimeField()),
                ('departure_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('departure_gate', models.CharField(blank=True, max_length=50, null=True)),
                ('arrival_airport', models.CharField(max_length=255)),
                ('arrival_airport_code', models.CharField(max_length=10)),
                ('arrival_scheduled', models.DateTimeField()),
                ('arrival_estimated', models.DateTimeField()),
                ('arrival_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('arrival_gate', models.CharField(blank=True, max_length=50, null=True)),
                ('departure_timezone', models.CharField(max_length=50)),
                ('arrival_timezone', models.CharField(max_length=50)),
            ],
        ),
    ]
