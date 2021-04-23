from django.urls import path
from . import views

urlpatterns = [
    path('get_places/', views.CountriesListView.as_view()),
    path('city/<int:pk>/', views.CityDetailView.as_view()),
    path('categories_by_city/<int:pk>/', views.CategoriesByCityView.as_view()),
    path('tours_list/', views.ToursByCityAndCategoryView.as_view()),
    path('tours_count_by_city/<int:pk>/', views.ToursCountByCityView.as_view()),
    path('tours_by_city/<int:pk>/', views.ToursByCityView.as_view()),
    path('tour/<int:pk>/', views.TourDetailView.as_view())
]



