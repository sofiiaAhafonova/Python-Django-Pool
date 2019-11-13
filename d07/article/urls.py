from django.urls import path, include
from article import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
]
