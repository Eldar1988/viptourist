from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Seller, Document, ForSellerNotification, SellerAction, ForAllSellersNotification


class DocumentsInline(admin.TabularInline):
    model = Document
    classes = ['collapse']
    readonly_fields = ('get_image', 'title', 'file', 'upload_date')
    extra = 0

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.file.url} style="height: 70px; width: 110px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


class SellerNotificationsInline(admin.TabularInline):
    model = ForSellerNotification
    classes = ['collapse']
    extra = 0


class SellerActionsInline(admin.TabularInline):
    model = SellerAction
    extra = 0
    classes = ['collapse']
    readonly_fields = ('seller', 'title', 'action', 'date')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'user', 'company', 'name', 'phone', 'whatsapp', 'email', 'active', 'balance', 'rating',
                    'register_date')
    list_editable = ('active',)
    list_filter = ('active', 'rating', 'register_date', 'updated')
    search_fields = ('name', 'company', 'phone', 'whatsapp')
    list_display_links = ('get_image', 'user', 'company', 'name')
    inlines = [DocumentsInline, SellerNotificationsInline, SellerActionsInline]
    # readonly_fields = ('get_image_full_size', 'company', 'name', 'phone', 'whatsapp', 'balance',
    #                    'register_date', 'updated', 'avatar')

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Photo'

    def get_image_full_size(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 250px; width: 250px; object-fit: cover; border-radius: 5px">')


@admin.register(ForAllSellersNotification)
class ForAllSellersNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated')
    search_fields = ('title',)
    list_filter = ('created_date', 'updated')
