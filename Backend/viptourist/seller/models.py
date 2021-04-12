from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from mainapp.models import AppUser


class Seller(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    whatsapp = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    avatar = ThumbnailerImageField(upload_to='sellers/', resize_source={'size': (300, 300), 'crop': 'scale'})
    active = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    register_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('register_date',)


class Document(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    title = models.CharField(max_length=255)
    file = ThumbnailerImageField(upload_to='seller_documents/', resize_source={'size': (700, 700), 'crop': 'scale'})
    confirmed = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('upload_date',)


class ForSellerNotification(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True, related_name='знерщт')
    title = models.CharField(max_length=255)
    text = models.TextField()
    confirmed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)


class SellerAction(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True, related_name='actions')
    title = models.CharField(max_length=255)
    action = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class ForAllSellersNotification(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)

