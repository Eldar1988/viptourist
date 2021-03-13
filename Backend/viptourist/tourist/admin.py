from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tourist, TourReview, ReviewPhoto


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'user', 'name', 'phone', 'whatsapp', 'active', 'balance', 'register_date')
    list_editable = ('active',)
    readonly_fields = ('get_image', 'user', 'name', 'phone', 'whatsapp', 'balance', 'register_date', 'updated',
                       'avatar')
    list_filter = ('active', 'register_date', 'updated')
    search_fields = ('name', 'phone', 'whatsapp')
    list_display_links = ('get_image', 'user', 'name')

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Avatar'
