from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
from .serializers import TravelSerializer, KlassSerializer, HotelSerializer
from .models import Hotel, Klass, Travel


class TravelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response({"travels": TravelSerializer(travel).data})
            except:
                return Response({"error": "Bunday id dagi kontent mavjud emas!"})

        travels = Travel.objects.all()
        return Response({"travels": TravelSerializer(travels, many=True).data})

    def post(self, request: Request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid()
        travel = serializer.save()
        return Response({"travels": TravelSerializer(travel).data, "message": "Travel add success!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                serializer = TravelSerializer(travel, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_travel = serializer.save()
                return Response({"travels": TravelSerializer(updated_travel).data, "message": "Travel success updated!"})
            except:
                return Response({'error': "Not found travel"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                travel.delete()
                return Response({'success': "Travel success delete!"})
            except:
                return Response({'error': "Not found travel"})

        return Response({"detail": "Method \"DELETE\" not allowed."})


class KlassAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response({"klasses": KlassSerializer(klass).data})
            except:
                return Response({"error": "Klass Not found!"})

        klasses = Klass.objects.all()
        return Response({"klasses": KlassSerializer(klasses, many=True).data})

    def post(self, request: Request):
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid()
        klass = serializer.save()
        return Response({"klasses": KlassSerializer(klass).data, "message": "Klass add success!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                serializer = KlassSerializer(klass, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_klass = serializer.save()
                return Response({"klasses": KlassSerializer(updated_klass).data, "message": "Klass success updated!"})
            except:
                return Response({'error': "Not found klass"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                klass.delete()
                return Response({'success': "Klass success delete!"})
            except:
                return Response({'error': "Not found klass"})

        return Response({"detail": "Method \"DELETE\" not allowed."})


class HotelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response({"hotels": HotelSerializer(hotel).data})
            except:
                return Response({"error": "Hotel Not found!"})

        hotels = Hotel.objects.all()
        return Response({"hotels": HotelSerializer(hotels, many=True).data})

    def post(self, request: Request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid()
        hotel = serializer.save()
        return Response({"hotels": HotelSerializer(hotel).data, "message": "Hotel add success!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                serializer = HotelSerializer(hotel, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_hotel = serializer.save()
                return Response({"hotels": HotelSerializer(updated_hotel).data, "message": "Hotel success updated!"})
            except:
                return Response({'error': "Not found hotel"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                hotel.delete()
                return Response({'success': "Hotel success delete!"})
            except:
                return Response({'error': "Not found hotel"})

        return Response({"detail": "Method \"DELETE\" not allowed."})