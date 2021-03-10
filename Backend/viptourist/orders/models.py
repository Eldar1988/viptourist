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

    tour_date = models.CharField(max_length=100, null=True, blank=True)
    tour_time = models.CharField(max_length=20, null=True, blank=True)
    tour_language = models.CharField(max_length=30, null=True, blank=True)

    adults = models.PositiveSmallIntegerField(default=1)
    children = models.PositiveSmallIntegerField(default=0)
    address = models.TextField(null=True, blank=True)

    purchase_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.tourist} - {self.offer}'

    class Meta:
        ordering = ('-purchase_date',)

