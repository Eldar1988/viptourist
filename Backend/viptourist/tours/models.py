from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField

from seller.models import Seller


class Category(models.Model):
    title = models.CharField('Category title', max_length=255, db_index=True)
    image = ThumbnailerImageField(upload_to='categories/', resize_source={'size': (400, 400), 'crop': 'scale'})
    slug = models.SlugField(unique=True, db_index=True)
    order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('order',)


class Country(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='cities')
    title = models.CharField(max_length=255, db_index=True)
    image = ThumbnailerImageField(upload_to='tours/', resize_source={'size': (400, 400), 'crop': 'scale'}, blank=True,
                                  null=True)
    slug = models.SlugField(db_index=True, unique=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ('order',)


class Tour(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='tours')
    category = models.ManyToManyField(Category, related_name='tours')
    title = models.CharField(max_length=255, db_index=True)
    image = ThumbnailerImageField(upload_to='tours/', resize_source={'size': (300, 300), 'crop': 'scale'})
    duration = models.DecimalField('Duration (hours)', max_digits=3, decimal_places=2, default=0)
    short_description = RichTextUploadingField()
    description = RichTextUploadingField()
    important_information = RichTextUploadingField(null=True)
    not_suitable_for = models.TextField(help_text='the list must be separated by commas', null=True)
    will_need = models.TextField(help_text='the list must be separated by commas', null=True)
    prohibited = models.TextField(help_text='the list must be separated by commas', null=True)
    views = models.IntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=5)
    active = models.BooleanField(default=False)
    publication_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publication_date',)


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = ThumbnailerImageField(upload_to='tours/', resize_source={'size': (1000, 1000), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ('order',)


class OfferLanguage(models.Model):
    language = models.CharField(max_length=50)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.language

    class Meta:
        ordering = ('order',)


class OfferTime(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

    class Meta:
        ordering = ('time',)


class Offer(models.Model):
    active = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='offers')
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True, related_name='offers')
    price = models.DecimalField('Price USD', max_digits=6, decimal_places=2)
    children_price = models.DecimalField('Children price USD', max_digits=6, decimal_places=2, null=True, blank=True)

    included = models.TextField(help_text='the list must be separated by commas')
    excluded = models.TextField(help_text='the list must be separated by commas')

    transfer = models.BooleanField(default=False)
    transfer_detail = models.TextField(null=True)

    languages = models.ManyToManyField(OfferLanguage, blank=True, related_name='offers')
    times = models.ManyToManyField(OfferTime, blank=True, related_name='offers')
    min_age = models.PositiveSmallIntegerField(default=2)
    max_age = models.PositiveSmallIntegerField(default=80)

    register_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Offer id: {self.id}. Seller: {self.seller}'

    class Meta:
        ordering = ('-register_date',)


class OfferImage(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = ThumbnailerImageField(upload_to='tours/', resize_source={'size': (1000, 1000), 'crop': 'scale'})

    def __str__(self):
        return f'{self.id}'
