from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CityListSerializer, CountrySerializer, TourListSerializer, CategoryListSerializer, \
    CitySearchListSerializer, TourDetailSerializer
from .models import Country, Category, City, Tour

from .service import ToursPagination


class CountriesListView(generics.ListAPIView):
    """Countries and cities view"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityDetailView(generics.RetrieveAPIView):
    """City Detail"""
    queryset = City.objects.all()
    serializer_class = CityListSerializer


class CategoriesByCityView(generics.ListAPIView):
    """Categories by city id"""
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        categories = Category.objects.filter(tours__city_id=self.kwargs['pk']).distinct()
        return categories


class ToursByCityAndCategoryView(generics.ListAPIView):
    """Tours list: params 'city=id', 'category=id'"""
    serializer_class = TourListSerializer

    def get_queryset(self):
        tours = Tour.objects.filter(city_id=self.request.query_params['city'], category__id=self.request.query_params['category'], future=True, active=True)
        return tours


class ToursCountByCityView(APIView):
    """Tours count by city id"""
    def get(self, request, pk):
        tours_count = Tour.objects.filter(city_id=pk).count()
        return HttpResponse(tours_count)


class ToursByCityView(generics.ListAPIView):
    """All tours by city id"""
    serializer_class = TourListSerializer
    pagination_class = ToursPagination

    def get_queryset(self):
        tours = Tour.objects.filter(city_id=self.kwargs['pk'])
        return tours


class TourDetailView(generics.RetrieveAPIView):
    """Tour detail by id"""
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
