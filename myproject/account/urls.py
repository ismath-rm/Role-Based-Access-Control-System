from django.urls import path
from account import views
urlpatterns = [
    path('flight-booking/',views.FlightBookingView.as_view(),name='flight-booking'),
    path('hotel-booking/',views.HotelBookingView.as_view(),name='hotel-booking'),
    path('assistant-flight-booking/',views.AssistantFlightBookingView.as_view(),name='assistant-flight-booking'),
    path('assistant-hotel-booking/',views.AssistantHotelBookingView.as_view(), name='assistant-hotel-booking'),
]
