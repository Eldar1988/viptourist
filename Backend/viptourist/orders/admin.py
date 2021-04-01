from django.contrib import admin
from .models import TourPurchase


@admin.register(TourPurchase)
class TourPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'tourist', 'seller', 'offer', 'tour', 'seller_confirmation', 'used', 'paid_out',
                    'total_cost', 'purchase_date', )
    list_editable = ('paid_out',)
    list_filter = ('seller_confirmation', 'used', 'paid_out', 'purchase_date', 'updated')
    search_fields = ('tourist__name', 'seller__company', 'seller__name', 'tour__title',)
