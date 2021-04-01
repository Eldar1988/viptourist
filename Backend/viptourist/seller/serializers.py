from rest_framework import serializers

from .models import Seller, Document, ForSellerNotification, ForAllSellersNotification


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        exclude = ('updated',)


class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        exclude = ('updated',)


class ForSellerNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForSellerNotification
        exclude = ('updated',)


class ForAllSellerNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForAllSellersNotification
        exclude = ('updated',)