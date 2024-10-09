from rest_framework import serializers
from .models import *

class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['name', 'name_uz','name_en','name_ru', 'description','description_uz','description_en','description_ru','image','created_at']

class OurSertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurSertificate
        fields = ['title', 'title_uz','title_en','title_ru', 'image']

class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClients
        fields = ['company_name', 'company_name_uz','company_name_en','company_name_ru', 'image']

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = ['title', 'title_uz','title_en','title_ru', 'description','description_uz','description_en','description_ru','image']

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['title', 'title_uz','title_en','title_ru', 'description','description_uz','description_en','description_ru']

class TariflarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariflar
        fields = ['plan', 'plan_uz','plan_en','plan_ru', 'description','description_uz','description_en','description_ru','price','get']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['savol','savol_uz','savol_en','savol_ru','javob','javob_uz','javob_en','javob_ru']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'title_uz','title_en','title_ru', 'description','description_uz','description_en','description_ru']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['fullname', 'fullname_uz','fullname_en','fullname_ru', 'description','description_uz','description_en','description_ru','image']



class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['title', 'title_uz','title_en','title_ru', 'cat','cat_uz','cat_en','cat_ru','image']

class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = ['fullname', 'fullname_uz', 'fullname_en', 'fullname_ru', 'job', 'job_uz','job_en', 'job_ru', 'image']

class NimaUchunBizSerializer(serializers.ModelSerializer):
    class Meta:
        model = NimaUchunBiz
        fields = ['title', 'title_uz','title_en','title_ru', 'description','description_uz','description_en','description_ru']

class CategorySerializer(serializers.ModelSerializer):
    xodim = XodimSerializer(read_only=True, many=True)
    kimlar_uchun = NimaUchunBizSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['title', 'xodim','kimlar_uchun']

class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True,many=True)
    class Meta:
        model = Services
        fields = ['title', 'title_uz', 'title_en', 'title_ru', 'category']

class ContactSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = ['fullname', 'fullname_uz', 'fullname_en', 'fullname_ru', 'phone','service','message','is_checked','created_at']