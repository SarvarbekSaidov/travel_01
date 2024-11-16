from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Travel, Class, Hotel
from .serializers import TravelSerializer, ClassSerializer, HotelSerializer
# Create your views here.

class TravelAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(travel)
        else:
            travels = Travel.objects.all()
            serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        travel = Travel.objects.get(pk=pk)
        serializer = TravelSerializer(travel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        travel = Travel.objects.get(pk=pk)
        travel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            travel_class = Class.objects.get(pk=pk)
            serializer = ClassSerializer(travel_class)
        else:
            classes = Class.objects.all()
            serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        travel_class = Class.objects.get(pk=pk)
        serializer = ClassSerializer(travel_class, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        travel_class = Class.objects.get(pk=pk)
        travel_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HotelAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            hotel = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(hotel)
        else:
            hotels = Hotel.objects.all()
            serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
