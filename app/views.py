from rest_framework import viewsets
from .models import Account, Locality, City, Account, PropertyType, Society
from .serializers import LocalitySerializer, CitySerialier, PropertyTypeSerializer, SocietySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerialier

class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

class PropertyTypeViewSet(viewsets.ModelViewSet):
	queryset = PropertyType.objects.all()
	serializer_class = PropertyTypeSerializer

class SocietyViewSet(viewsets.ModelViewSet):
	queryset = Society.objects.all()
	serializer_class = SocietySerializer