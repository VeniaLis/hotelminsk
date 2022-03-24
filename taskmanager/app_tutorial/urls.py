from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('hotel_detail/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel_list/', views.hotel_list, name='hotel_list'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review_list/', views.review_list, name='review_list'),
]