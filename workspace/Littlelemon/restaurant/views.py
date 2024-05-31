from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
   return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer
   

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
   serializer_class = BookingSerializer
   queryset = Booking.objects.all()
   permission_classes = [IsAuthenticated]