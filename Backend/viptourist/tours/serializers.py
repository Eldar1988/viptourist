from rest_framework import serializers
from .models import Country, City, Tour, Category, TourImage


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        exclude = ('order',)


class CountrySerializer(serializers.ModelSerializer):
    cities = CityListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class TourListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ('id', 'title', 'image', 'rating', 'reviews_count', 'offers_minimal_price')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class CitySearchListSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='title', read_only=True, many=False)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'slug')


class TourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourImage
        fields = ('id', 'image')


class TourDetailSerializer(serializers.ModelSerializer):
    images = TourImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        exclude = ('active', 'future', 'order', 'update_date')


