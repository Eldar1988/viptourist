from modeltranslation.translator import register, TranslationOptions
from .models import Faq, HomeSlide


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(HomeSlide)
class HomeSlideTranslationOptions(TranslationOptions):
    fields = ('title',)

