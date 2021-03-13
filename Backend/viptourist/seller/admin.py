from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Seller, Document


class DocumentsInline(admin.TabularInline):
    model = Document
    readonly_fields = ('get_image', 'title', 'file', 'upload_date')
    extra = 0

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.file.url} style="height: 70px; width: 110px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'user', 'company', 'name', 'phone', 'whatsapp', 'active', 'balance', 'register_date')
    list_editable = ('active',)
    list_filter = ('active', 'register_date', 'updated')
    search_fields = ('name', 'company', 'phone', 'whatsapp')
    list_display_links = ('get_image', 'user', 'company', 'name')
    inlines = [DocumentsInline]
    readonly_fields = ('get_image', 'user', 'company', 'name', 'phone', 'whatsapp', 'balance',
                       'register_date', 'updated', 'avatar')

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Photo'


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('seller', 'title', 'file', 'confirmed', 'upload_date', 'updated')
    list_editable = ('confirmed',)
    search_fields = ('title',)
    list_filter = ('upload_date', 'updated')
