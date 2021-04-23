from django.db.models import signals
from django.dispatch import receiver
from django.db.models import Min

from .models import Offer, Tour


def get_min_price(obj) -> None:
    """Получение минимальной цены офферов тура"""
    try:
        tour = Tour.objects.get(id=obj.tour_id)     # Тур оффера
        offers = Offer.objects.filter(tour_id=tour.id)      # Все офферы тура
        min_price = offers[0].price     # Дефолтная минимальная цена офферов

        for offer in offers:
            if offer.price < min_price:
                min_price = offer.price

        tour.offers_minimal_price = min_price
        tour.save()
    except:
        return


@receiver(signals.post_save, sender=Offer)
def handler(sender, instance, **kwargs) -> None:
    get_min_price(instance)
