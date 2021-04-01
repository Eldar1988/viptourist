from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CityListSerializer, CountrySerializer, TourListSerializer, CategoryListSerializer, \
    CitySearchListSerializer
from .models import Country, Category, City, Tour


class CountriesListView(APIView):

    def get(self, request):
        """Countries > Cities list"""
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)

        return Response(serializer.data)


class ToursListSortedByCategoryView(APIView):
    """Tours list sorted by category. Filters: city :str, price :float, start_time :str """
    def get(self, request, city_slug):
        categories = Category.objects.filter(tours__city__slug=city_slug).distinct()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)
