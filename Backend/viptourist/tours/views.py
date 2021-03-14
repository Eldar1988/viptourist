from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CityListSerializer, CountrySerializer, TourListSerializer, CategoryListSerializer, \
    CitySearchListSerializer
from .models import Country, Category, City, Tour


class CountriesListView(APIView):

    def get(self, request):
        """Countries > Cities list"""
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)

        return Response(serializer.data)


class ToursListSortedByCategoryView(generics.ListAPIView):
    """Tours list sorted by category. Filters: city :str, price :float, start_time :str """
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        city_slug = self.kwargs['city_slug']
        return Category.objects.filter(tours__city__slug=city_slug).distinct()
