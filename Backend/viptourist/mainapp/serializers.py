from rest_framework import serializers
from .models import HomeSlide, Faq, Contact


class HomeSlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeSlide
        exclude = ('order',)


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        exclude = ('order',)


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
