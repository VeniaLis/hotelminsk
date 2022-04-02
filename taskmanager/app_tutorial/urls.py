from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('hotel_detail/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel_list/', views.hotel_list, name='hotel_list'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review_list/', views.review_list, name='review_list'),
    path('hotel_review_list/<int:hotel_id>/', views.hotel_review_list, name='hotel_review_list'),
    path('add_hotel/', views.add_hotel, name='add_hotel'),
    path('edit_hotel/<int:hotel_id>/', views.edit_hotel, name='edit_hotel'),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('add_review/<int:hotel_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]