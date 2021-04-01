from django.urls import path
from . import views


urlpatterns = [
    path('seller_detail/', views.SellerDetailView.as_view()),
    path('seller_notifications/<int:pk>', views.SellerNotificationsView.as_view())
]