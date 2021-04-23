from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Tourist, TourReview, ReviewPhoto, ForTouristNotification, ForAllTouristNotification, TouristAction


class TourReviewsInline(admin.TabularInline):
    model = TourReview
    extra = 0
    classes = ['collapse']
    readonly_fields = ('tour', 'offer', 'seller', 'rating', 'text')
    show_change_link = ('tour',)


class TouristNotificationsInline(admin.TabularInline):
    model = ForTouristNotification
    classes = ['collapse']
    extra = 0


class TouristActionsInline(admin.TabularInline):
    model = TouristAction
    extra = 0
    classes = ['collapse']
    readonly_fields = ('tourist', 'title', 'action', 'date')


class ReviewPhotoInline(admin.TabularInline):
    model = ReviewPhoto
    extra = 0
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Miniature'


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'user', 'name', 'phone', 'whatsapp', 'email', 'active', 'balance', 'register_date')
    list_editable = ('active',)
    readonly_fields = ('get_image_full_size', 'user', 'name', 'phone', 'whatsapp', 'balance', 'register_date', 'updated',
                       'avatar')
    list_filter = ('active', 'register_date', 'updated')
    search_fields = ('name', 'phone', 'whatsapp')
    list_display_links = ('get_image', 'user', 'name')
    inlines = [TourReviewsInline, TouristActionsInline, TouristNotificationsInline]

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Avatar'

    def get_image_full_size(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="height: 250px; width: 250px; object-fit: cover; border-radius: 5px">')

    get_image.short_description = 'Avatar'


@admin.register(TourReview)
class TourReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'offer', 'seller', 'tourist', 'rating', 'public', 'date')
    # readonly_fields = ('id', 'tour', 'offer', 'seller', 'tourist', 'rating', 'date', 'text')
    list_editable = ('public',)
    search_fields = ('tour__title', 'seller__name', 'seller__company', 'text')
    list_filter = ('public', 'rating')
    save_as = True

    inlines = [ReviewPhotoInline]


@admin.register(ForAllTouristNotification)
class ForAllTouristNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated')
    search_fields = ('title',)
    list_filter = ('created_date', 'updated')
