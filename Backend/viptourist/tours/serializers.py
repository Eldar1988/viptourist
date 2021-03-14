from rest_framework import serializers
from .models import Country, City, Tour, Category


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        exclude = ('order', 'country')


class CountrySerializer(serializers.ModelSerializer):
    cities = CityListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class TourListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ('id', 'title', 'image', 'duration', 'views', 'rating')


class CategoryListSerializer(serializers.ModelSerializer):
    tours = TourListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'tours')


class CitySearchListSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='title', read_only=True, many=False)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'slug')



