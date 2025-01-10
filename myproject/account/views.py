from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsAdmin,IsManager,IsCorporateOrPremiumUser,IsNormalUser
# Create your views here.

class FlightBookingView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = []

    def get(self,request):
        return Response({"message": "Access to Flight Booking Page"})


class HotelBookingView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = []

    def get(self,request):
        return Response({"message": "Access to Hotel Booking Page"})
    
class AssistantFlightBookingView(APIView):
    # permission_classes = [IsAuthenticated & (IsAdmin | IsManager | IsCorporateOrPremiumUser)]
    permission_classes = []

    def get(self,request):
        return Response({"message": "Access to Assistant Flight Booking Page"})


class AssistantHotelBookingView(APIView):
    # permission_classes = [IsAuthenticated & (IsAdmin | IsManager | IsCorporateOrPremiumUser)]
    permission_classes = []

    def get(self,request):
        return Response({"message": "Access to Assistant Hotel Booking Page"})