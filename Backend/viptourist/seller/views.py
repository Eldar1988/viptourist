from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SellerSerializer, ForSellerNotificationSerializer
from .models import Seller, ForSellerNotification


class SellerDetailView(APIView):

    def get(self, request):
        """Seller profile information by request user"""
        seller = Seller.objects.get(user=request.user.id)
        serializer = SellerSerializer(seller, many=False)
        return Response(serializer.data)


class SellerNotificationsView(APIView):

    def get(self, request, pk):
        """Get seller notifications by seller id"""
        notifications = ForSellerNotification.objects.filter(seller_id=pk)
        serializer = ForSellerNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
