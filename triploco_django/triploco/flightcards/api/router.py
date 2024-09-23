from django.urls import path

from flightcards.api.views import OCRApiView
from flightcards.api.views import FlightListAPIView

urlpatterns = [
    path("ocr/", OCRApiView.as_view()),
    path('flights/', FlightListAPIView.as_view(), name='flight-list'),
]