from django.contrib import admin
from flightcards.models import Flight
# Register your models here.

@admin.register(Flight)
class UserAdmin(admin.ModelAdmin):
    list_display = ['flight_date','flight_status','airline_name','airline_iata','airline_icao']
