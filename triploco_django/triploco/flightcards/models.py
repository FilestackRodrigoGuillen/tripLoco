from django.db import models

class Flight(models.Model):
    # Datos del vuelo
    flight_date = models.DateField()
    flight_status = models.CharField(max_length=50)
    
    # Datos de la aerolínea
    airline_name = models.CharField(max_length=255)
    airline_iata = models.CharField(max_length=50)
    airline_icao = models.CharField(max_length=40)
    
    # Información del vuelo
    flight_number = models.CharField(max_length=20)
    flight_iata = models.CharField(max_length=20)
    flight_icao = models.CharField(max_length=20)

    # Datos de salida
    departure_airport = models.CharField(max_length=255)
    departure_airport_code = models.CharField(max_length=20)
    departure_scheduled = models.DateTimeField()
    departure_estimated = models.DateTimeField()
    departure_terminal = models.CharField(max_length=50, null=True, blank=True)
    departure_gate = models.CharField(max_length=50, null=True, blank=True)

    # Datos de llegada
    arrival_airport = models.CharField(max_length=255)
    arrival_airport_code = models.CharField(max_length=10)
    arrival_scheduled = models.DateTimeField()
    arrival_estimated = models.DateTimeField()
    arrival_terminal = models.CharField(max_length=50, null=True, blank=True)
    arrival_gate = models.CharField(max_length=50, null=True, blank=True)

    # Zona horaria para el pie de página
    departure_timezone = models.CharField(max_length=50)
    arrival_timezone = models.CharField(max_length=50)
    
    ocr_workflow = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Flight {self.flight_iata} - {self.flight_date}"
