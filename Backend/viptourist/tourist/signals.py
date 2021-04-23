from django.db.models import signals
from django.dispatch import receiver
from .models import TourReview
from django.db.models import Avg
from tours.models import Tour, Offer
from seller.models import Seller


def ratings_update(obj):
    try:
        tour = Tour.objects.get(id=obj.tour_id)
        tour_ratings_average = TourReview.objects.filter(tour_id=obj.tour_id).aggregate(Avg('rating'))
        tour.rating = round(tour_ratings_average['rating__avg'], 1)
        tour.reviews_count = TourReview.objects.filter(tour_id=obj.tour_id).count()
        tour.save()

        offer = Offer.objects.get(id=obj.offer_id)
        offer_ratings_average = TourReview.objects.filter(offer_id=obj.offer_id).aggregate(Avg('rating'))
        offer.rating = round(offer_ratings_average['rating__avg'], 1)
        offer.reviews_count = TourReview.objects.filter(offer_id=obj.offer_id).count()
        offer.save()

        seller = Seller.objects.get(id=obj.seller_id)
        seller_ratings_average = TourReview.objects.filter(seller_id=obj.seller_id).aggregate(Avg('rating'))
        seller.rating = round(seller_ratings_average['rating__avg'], 1)
        seller.reviews_count = TourReview.objects.filter(seller_id=obj.seller_id).count()
        seller.save()

    except:
        return


@receiver(signals.post_delete, sender=TourReview)
def handler(sender, instance, **kwargs):
    ratings_update(instance)


@receiver(signals.post_save, sender=TourReview)
def handler(sender, instance, **kwargs):
    ratings_update(instance)
