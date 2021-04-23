from django.db.models import Avg
from tours.models import Tour, Offer
from seller.models import Seller


def ratings_update(obj, TourReview, delete=False):
    print(delete)
    tour = Tour.objects.get(id=obj.tour_id)
    tour_ratings_average = TourReview.objects.filter(tour_id=obj.tour_id).aggregate(Avg('rating'))
    tour.rating = round(tour_ratings_average['rating__avg'], 2)

    offer = Offer.objects.get(id=obj.offer_id)
    offer_ratings_average = TourReview.objects.filter(offer_id=obj.offer_id).aggregate(Avg('rating'))
    offer.rating = round(offer_ratings_average['rating__avg'], 2)

    seller = Seller.objects.get(id=obj.seller_id)
    seller_ratings_average = TourReview.objects.filter(seller_id=obj.seller_id).aggregate(Avg('rating'))
    seller.rating = round(seller_ratings_average['rating__avg'], 2)

    if delete:
        tour.reviews_count -= 1
        offer.reviews_count -= 1
        seller.reviews_count -= 1

    else:
        tour.reviews_count += 1
        offer.reviews_count += 1
        seller.reviews_count += 1

    seller.save()
    tour.save()
    offer.save()
