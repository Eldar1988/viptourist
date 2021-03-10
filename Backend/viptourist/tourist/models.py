from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from tours.models import Tour, Offer
from seller.models import Seller


class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tourist')
    name = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=25)
    whatsapp = models.CharField(max_length=25)
    avatar = ThumbnailerImageField(upload_to='tourists_avatars/', resize_source={'size': (400, 400), 'crop': 'scale'})
    active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    register_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-register_date',)


class TourReview(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    tourist = models.ForeignKey(Tourist, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    text = models.TextField('Review text')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tour} - {self.seller} - {self.tourist}'

    class Meta:
        ordering = ('-date',)


class ReviewPhoto(models.Model):
    review = models.ForeignKey(TourReview, on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    image = ThumbnailerImageField(upload_to='review_photos/', resize_source={'size': (800, 800), 'crop': 'scale'})
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review}'

    class Meta:
        ordering = ('-date',)
