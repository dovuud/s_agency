from django.urls import path
from .views import *

urlpatterns = [
    path('whyus/',WhyUsView.as_view(),name='whyus'),
    path('whyus/<int:pk>/', WhyUsView.as_view(),name='whyus-detail'),
    path('oursertificate/',OurSertificatesView.as_view(),name='oursertificates'),
    path('ourclients/',OurClientsView.as_view(),name='ourclients'),
    path('ourservices/',OurServicesView.as_view(),name='ourservices'),
    path('pricelist/',PriceListView.as_view(),name='pricelist'),
    path('tariflar/',TariflarView.as_view(),name='tariflar'),
    path('faq/',FAQView.as_view(),name='faq'),
    path('about/',AboutView.as_view(),name='about'),
    path('feedback/',FeedbackView.as_view(),name='feedback'),
    path('portfolio/',PortfolioView.as_view(),name='portfolio'),
    path('xodim/',XodimView.as_view(),name='xodim'),
    path('nimauchunbiz/',NimaUchunBizView.as_view(),name='nimauchunbiz'),

    path('category/',CategoryView.as_view(),name='category'),
    path('service/',ServicesView.as_view(),name='service'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('contact/<int:pk>/', ContactDetailView.as_view(),name='contact-detail'),
]