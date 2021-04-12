from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class AppUser(models.Model):
    """Пользователи приложения Google Firebase"""
    user_id = models.CharField('User ID', max_length=255, db_index=True)
    is_seller = models.BooleanField(default=False)
    is_tourist = models.BooleanField(default=False)
    register_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ('-register_date',)


class HomeSlide(models.Model):
    image = ThumbnailerImageField(upload_to='home_slides/', resize_source={'size': (1000, 1000), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'slide {self.id}'

    class Meta:
        ordering = ('order',)


class Faq(models.Model):
    question = models.CharField(max_length=255, db_index=True)
    answer = models.TextField()
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'FAQ'
        verbose_name = 'FAQ'
        ordering = ('order',)


class Contact(models.Model):
    phone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=20, help_text='Format: 7**********')
    email = models.EmailField()

    def __str__(self):
        return f'Contact information v{self.id}'
