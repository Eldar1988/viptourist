from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, OrderedDict

from .models import Category, Country, City, Tour, TourImage, Offer, OfferLanguage, OfferTime, OfferImage, OfferDate

admin.site.register(OfferLanguage)
admin.site.register(OfferTime)
admin.site.register(OfferDate)


class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'seller', 'price', 'active', 'rating', 'register_date')
    list_editable = ('active',)
    list_filter = ('active', 'languages', 'seller', 'everyday', ('register_date', DateTimeRangeFilter),
                   ('updated', DateTimeRangeFilter))
    search_fields = ('tour__title', 'seller__name')
    filter_horizontal = ('languages', 'times')

    inlines = [OfferImageInline]
    readonly_fields = ('rating', 'reviews_count')

    save_as = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order')
    list_editable = ('order',)
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 70px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'

    save_as = True


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('slug',)
    search_fields = ('title',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'country', 'order')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('order',)
    list_filter = (('country', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('title',)
    readonly_fields = ('get_medium_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    def get_medium_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 150px; width: 210px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'
    get_medium_image.short_description = 'Miniature'


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


class OfferInline(admin.TabularInline):
    model = Offer
    extra = -1
    can_delete = False
    show_change_link = ('pk',)
    fields = ('tour', 'seller', 'price', 'active', 'register_date')
    readonly_fields = ('tour', 'seller', 'price', 'register_date')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'city', 'active', 'future', 'views', 'rating',
                    'get_tour_offers_count', 'offers_minimal_price', 'publication_date')
    search_fields = ('title', 'city__title')
    list_editable = ('active', 'future')
    list_display_links = ('get_image', 'title')
    list_filter = ('active', 'future', ('category', admin.RelatedOnlyFieldListFilter),
                   ('publication_date', DateTimeRangeFilter), ('update_date', DateTimeRangeFilter),)
    readonly_fields = ('get_image', 'views', 'offers_minimal_price', 'reviews_count', 'rating')
    inlines = [TourImageInline, OfferInline]
    filter_horizontal = ('category',)
    ordering = ('-publication_date',)

    def get_tour_offers_count(self, obj) -> int:
        offers_count = Offer.objects.filter(tour_id=obj.id).count()
        return offers_count

    def get_image(self, obj) -> str:
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; width: 70px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'
    get_tour_offers_count.short_description = 'Offers'

    save_as = True
