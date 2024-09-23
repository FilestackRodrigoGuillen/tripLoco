from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from flightcards.models import Flight
from flightcards.api.serializers import FlightSerializer
from .constants import AVION_STACK_API_KEY

def extract_flight_number_from_json(data):
    iterator = 0
    flightnumber = ""
    current_word = ""
    text_areas = data.get('text', {}).get('results', {}).get('ocr_1725480279953', {}).get('data', {}).get('document', {}).get('text_areas')
    for area in text_areas:
        lines = area.get('lines')
        iterator = 0
        for line in lines:
            iterator += 1
            if iterator == 2 and current_word=="FLIGHT :":
                flightnumber=line.get("text")
            current_word = line.get("text")
    print(flightnumber)
    return flightnumber
    
    
class OCRApiView(APIView):
    def post(self, request, *args, **kwargs):
        received_json = request.data

        #EXTRACT FLIGHT INFORMATION
        flight_iata = extract_flight_number_from_json(received_json)
        access_key = AVION_STACK_API_KEY
        
        #SAVE THE JOB ID
        job_id = received_json.get("text").get("jobid")

        if not flight_iata:
            return Response(data={"error": "flight_iata is required"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        #GET FLIGHT DATA USING AVIONSTACK
        flight_data = fetch_flight_data(flight_iata, access_key)
        
        if flight_data is not None:
            flight_info = flight_data.get('data', [])[0] if flight_data.get('data') else None

            if flight_info:
                # SAVE INFO IN DATABASE
                flight = Flight.objects.create(
                    flight_date=flight_info.get("flight_date"),
                    flight_status=flight_info.get("flight_status"),
                    airline_name=flight_info["airline"].get("name"),
                    airline_iata=flight_info["airline"].get("iata"),
                    airline_icao=flight_info["airline"].get("icao"),
                    flight_number=flight_info["flight"].get("number"),
                    flight_iata=flight_info["flight"].get("iata"),
                    flight_icao=flight_info["flight"].get("icao"),
                    departure_airport=flight_info["departure"].get("airport"),
                    departure_airport_code=flight_info["departure"].get("iata"),
                    departure_scheduled=flight_info["departure"].get("scheduled"),
                    departure_estimated=flight_info["departure"].get("estimated"),
                    departure_terminal=flight_info["departure"].get("terminal"),
                    departure_gate=flight_info["departure"].get("gate"),
                    arrival_airport=flight_info["arrival"].get("airport"),
                    arrival_airport_code=flight_info["arrival"].get("iata"),
                    arrival_scheduled=flight_info["arrival"].get("scheduled"),
                    arrival_estimated=flight_info["arrival"].get("estimated"),
                    arrival_terminal=flight_info["arrival"].get("terminal"),
                    arrival_gate=flight_info["arrival"].get("gate"),
                    departure_timezone=flight_info["departure"].get("timezone"),
                    arrival_timezone=flight_info["arrival"].get("timezone"),
                    ocr_workflow=job_id
                )

                # RETURN JSON WITH THE FLIGHT DATA
                return Response(data=flight_data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={"error": "No flight data found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data={"error": "Failed to fetch data from external API"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def fetch_flight_data(flight_iata, access_key, limit=1):
    url = f"https://api.aviationstack.com/v1/flights?access_key={access_key}&flight_iata={flight_iata}&limit={limit}"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Error")
    except requests.exceptions.RequestException as e:
        print("Error fetching data from AvionStack")
        return None

class FlightListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener el parámetro de filtro desde la solicitud GET
        ocr_workflow = request.query_params.get('ocr_workflow', None)
        
        # Filtrar los vuelos según el ocr_workflow
        if ocr_workflow:
            flights = Flight.objects.filter(ocr_workflow=ocr_workflow)
        else:
            flights = Flight.objects.all()

        # Serializar los datos
        serializer = FlightSerializer(flights, many=True)
        
        # Devolver los datos serializados en la respuesta
        return Response(serializer.data, status=status.HTTP_200_OK)