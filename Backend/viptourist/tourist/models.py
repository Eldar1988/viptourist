from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models import signals
from django.dispatch import receiver


from tours.models import Tour, Offer
from seller.models import Seller
from mainapp.models import AppUser

from .models_service import ratings_update


class Tourist(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=25)
    whatsapp = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    avatar = ThumbnailerImageField(upload_to='tourists_avatars/', resize_source={'size': (400, 400), 'crop': 'scale'})
    active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
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
    public = models.BooleanField(default=False)
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


class ForTouristNotification(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    title = models.CharField(max_length=255)
    text = models.TextField()
    confirmed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)


class TouristAction(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.SET_NULL, null=True, blank=True, related_name='actions')
    title = models.CharField(max_length=255)
    action = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class ForAllTouristNotification(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)
