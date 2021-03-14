from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Country, City, Tour, TourImage, Offer, OfferLanguage


admin.site.register(OfferLanguage)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'seller', 'price', 'active', 'register_date')
    list_editable = ('active',)
    list_filter = ('active', 'languages', 'tour', 'seller', 'register_date', 'updated')
    search_fields = ('tour__title', 'seller__name')
    filter_horizontal = ('languages',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order')
    list_editable = ('slug', 'order')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 70px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_editable = ('slug',)
    search_fields = ('title',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'country', 'slug', 'order')
    list_editable = ('slug', 'order')
    list_filter = ('country',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 70px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 0
    show_change_link = ('seller',)
    fields = ('tour', 'seller', 'price', 'active', 'register_date')
    readonly_fields = ('tour', 'seller', 'price', 'register_date')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'city', 'active', 'duration', 'views', 'publication_date')
    search_fields = ('title',)
    list_editable = ('active',)
    list_display_links = ('get_image', 'title')
    list_filter = ('city', 'category', 'publication_date', 'update_date')
    readonly_fields = ('get_image', 'views', 'rating')
    inlines = [OfferInline, TourImageInline]
    filter_horizontal = ('category',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'

    save_as = True
