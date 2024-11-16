from django.urls import path
from .views import TravelAPIView, ClassAPIView, HotelAPIView

urlpatterns = [
    path('travels/', TravelAPIView.as_view(), name='travel-list-create'),
    path('travels/<int:pk>/', TravelAPIView.as_view(), name='travel-detail'),
    path('classes/', ClassAPIView.as_view(), name='class-list-create'),
    path('classes/<int:pk>/', ClassAPIView.as_view(), name='class-detail'),
    path('hotels/', HotelAPIView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelAPIView.as_view(), name='hotel-detail'),
]
