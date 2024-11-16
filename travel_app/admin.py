from django.contrib import admin
from .models import Class, Hotel, Travel
# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'star_rating', 'price')

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'price', 'travel_class', 'hotel')
    list_filter = ('travel_class', 'hotel')
    search_fields = ('name', 'description')
