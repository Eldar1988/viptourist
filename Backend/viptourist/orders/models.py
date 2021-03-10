from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from tours.models import Offer
from tourist.models import Tourist


class TourPurchase(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.SET_NULL, null=True, blank=True, related_name='tour_purchases')
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True, related_name='tour_purchases')
    seller_confirmation = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    qr_code = ThumbnailerImageField(upload_to='qr-codes/', resize_source={'size': (400, 400), 'crop': 'scale'})
    purchase_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tourist} - {self.offer}'

    class Meta:
        ordering = ('-purchase_date',)

