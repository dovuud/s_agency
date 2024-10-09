from modeltranslation.translator import register,TranslationOptions
from .models import *

@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
@register(OurSertificate)
class OurSertificatesTranslationOptions(TranslationOptions):
    fields = ('title', )
@register(OurClients)
class OurClientsTranslationOptions(TranslationOptions):
    fields = ('company_name', )
@register(OurServices)
class OurServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
@register(PriceList)
class PriceListTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
@register(Tariflar)
class TariflarTranslationOptions(TranslationOptions):
    fields = ('plan', 'description')
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('savol', 'javob')
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', )
@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('fullname', 'description')
@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'cat')

@register(Xodim)
class XodimTranslationOptions(TranslationOptions):
    fields = ('fullname', 'job' )
@register(NimaUchunBiz)
class NimaUchunBizTranslationOptions(TranslationOptions):
    fields = ('title', 'description')



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', )
@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('fullname', )