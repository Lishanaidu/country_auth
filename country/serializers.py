from rest_framework import serializers
from .models import Country
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name', 'population', 'latitude', 'longitude']
