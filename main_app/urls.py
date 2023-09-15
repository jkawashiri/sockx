from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('shoes/', views.ShoeList.as_view(), name='index'),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
]