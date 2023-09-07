from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),  # 이 부분이 중요합니다.
    path('cartype/', views.cartype, name='cartype'),
] 
