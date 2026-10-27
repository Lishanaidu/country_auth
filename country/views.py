from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Country
from .serializers import CountrySerializer

@api_view(['GET', 'POST'])
def country_list(request):
    """
    GET: Return a list of all countries.
    POST: Create a new country.
    """
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

