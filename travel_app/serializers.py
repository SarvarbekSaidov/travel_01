from rest_framework import serializers
from .models import Travel, Class, Hotel

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    travel_class = ClassSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Travel
        fields = '__all__'
