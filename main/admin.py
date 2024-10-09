from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
# Register your models here.


class WhyUsAdmin(TranslationAdmin):
    list_display = ('title', 'description')

class OurSertificateAdmin(TranslationAdmin):
    list_display = ('title', )

class OurClientsAdmin(TranslationAdmin):
    list_display = ('company_name', )

class OurServiceAdmin(TranslationAdmin):
    list_display = ('title', 'description')

class PriceListAdmin(TranslationAdmin):
    list_display = ('title', 'description')

class TariflarAdmin(TranslationAdmin):
    list_display = ('plan', 'description')

class FAQAdmin(TranslationAdmin):
    list_display = ('savol', 'javob')

class AboutAdmin(TranslationAdmin):
    list_display = ('title', )

class FeedbackAdmin(TranslationAdmin):
    list_display = ('fullname', 'description')

class PortfolioAdmin(TranslationAdmin):
    list_display = ('title', 'cat')

class XodimAdmin(TranslationAdmin):
    list_display = ('fullname', 'job')

class NimaUchunBizAdmin(TranslationAdmin):
    list_display = ('title', 'description')




class CategoryAdmin(TranslationAdmin):
    list_display = ('title', )

class ServiceAdmin(TranslationAdmin):
    list_display = ('title', )

class ContactAdmin(TranslationAdmin):
    list_display = ('fullname', )



admin.site.register(WhyUs, WhyUsAdmin)
admin.site.register(OurSertificate, OurSertificateAdmin)
admin.site.register(OurClients, OurClientsAdmin)
admin.site.register(OurServices, OurServiceAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Tariflar, TariflarAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Xodim, XodimAdmin)
admin.site.register(NimaUchunBiz, NimaUchunBizAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Services,ServiceAdmin)
admin.site.register(Contact,ContactAdmin)