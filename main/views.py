from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.


class WhyUsView(generics.ListCreateAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer

class WhyUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer

class OurSertificatesView(generics.ListCreateAPIView):
    queryset = OurSertificate.objects.all()
    serializer_class = OurSertificateSerializer

class OurClientsView(generics.ListAPIView):
    queryset = OurClients.objects.all()
    serializer_class = OurClientSerializer

class OurServicesView(generics.ListCreateAPIView):
    queryset = OurServices.objects.all()
    serializer_class = OurServiceSerializer

class PriceListView(generics.ListAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

class TariflarView(generics.ListAPIView):
    queryset = Tariflar.objects.all()
    serializer_class = TariflarSerializer

class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class FeedbackView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class PortfolioView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class XodimView(generics.ListAPIView):
    queryset = Xodim.objects.all()
    serializer_class = XodimSerializer

class NimaUchunBizView(generics.ListAPIView):
    queryset = NimaUchunBiz.objects.all()
    serializer_class = NimaUchunBizSerializer



class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ServicesView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer