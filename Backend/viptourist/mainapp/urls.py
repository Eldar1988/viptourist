from django.urls import path
from . import views


urlpatterns = [
    path('home_slides/', views.SlidesListView.as_view()),
    path('contacts/', views.ContactsView.as_view()),
    path('faq/', views.FaqView.as_view()),
    path('search_faq/', views.SearchFagView.as_view())
]