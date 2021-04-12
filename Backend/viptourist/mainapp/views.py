from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeSlide, Faq, Contact
from .serializers import HomeSlideSerializer, FaqSerializer, ContactsSerializer


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

    def get(self, request):
        """Contacts information"""
        contacts = Contact.objects.last()
        serializer = ContactsSerializer(contacts, many=False)
        return Response(serializer.data)

