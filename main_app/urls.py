from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('shoes/', views.ShoeList.as_view(), name='index'),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_review/', views.add_review, name='add_review'),
    path('shoes/<int:shoe_id>/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('shoes/<int:shoe_id>/add_bid/', views.add_bid, name='add_bid'),
    path('shoes/<int:shoe_id>/delete_bid/<int:bid_id>/', views.delete_bid, name='delete_bid'),
    path('search_shoes', views.search_shoes, name='search_shoes'),
    path('shoes/<int:shoe_id>/add_photo/', views.add_photo, name='add_photo'),
]