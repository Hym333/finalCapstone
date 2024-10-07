from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('articles/', views.articles, name='articles'),
    # path('charts', views.charts, name='charts'),
]