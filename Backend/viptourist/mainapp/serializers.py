from rest_framework import serializers
from .models import HomeSlide, Faq, Contact, PrivacyPolicy, PublicOffer


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


class PublicOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicOffer
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'

