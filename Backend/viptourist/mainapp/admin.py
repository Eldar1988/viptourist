from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import HomeSlide, Faq, Contacts


admin.site.register(Contacts)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    search_fields = ('question', 'answer')


@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'order')
    list_editable = ('order',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 70px; width: 110px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


admin.site.site_title = 'VIP Tourist'
admin.site.site_header = 'VIP Tourist - administration'
