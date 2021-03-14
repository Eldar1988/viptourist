from django.urls import path
from . import views

urlpatterns = [
    path('get_places/', views.CountriesListView.as_view()),
    path('get_tours_sorted_by_category/<slug:city_slug>', views.ToursListSortedByCategoryView.as_view())
]



