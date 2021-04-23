from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeSlide, Faq, Contact, PrivacyPolicy, PublicOffer
from .serializers import HomeSlideSerializer, FaqSerializer, ContactsSerializer, PrivacyPolicySerializer, PublicOfferSerializer


class SlidesListView(generics.ListAPIView):
    """Home page slides"""
    queryset = HomeSlide.objects.all()
    serializer_class = HomeSlideSerializer


class FaqView(generics.ListAPIView):
    """FAQ list"""
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class SearchFagView(APIView):

    def get(self, request):
        """FAQ by search. Params: search=str"""
        faq = Faq.objects.filter(question__icontains=request.GET.get('search'))
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data)


class ContactsView(APIView):
    """Contacts information view"""

    def get(self, request):
        """Contacts information"""
        contacts = Contact.objects.last()
        serializer = ContactsSerializer(contacts, many=False)
        return Response(serializer.data)


class PolicyView(APIView):
    """Privacy policy & Public offer view"""

    def get(self, request):
        response_data = {}
        policy = PrivacyPolicy.objects.last()
        policy_serializer = PrivacyPolicySerializer(policy, many=False)
        response_data['policy'] = policy_serializer.data

        offer = PublicOffer.objects.last()
        offer_serializer = PublicOfferSerializer(offer, many=False)
        response_data['offer'] = offer_serializer.data

        return Response(response_data)

