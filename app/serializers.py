from rest_framework import serializers
from .models import Locality, City, Account, PropertyType, Society


class CitySerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')

class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locality
        fields = ('__all__')

class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PropertyType
		fields = ('__all__')


class SocietySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Society
		fields = ('__all__')