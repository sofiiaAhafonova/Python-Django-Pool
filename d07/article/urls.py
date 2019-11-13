from django.urls import path, include
from article import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('publications/', views.PublicationsView.as_view(), name='publications'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('favorites/', views.FavoritesView.as_view(), name='favorites'),
    path('add_favorite/', views.AddFavoriteView.as_view(), name='favorites'),

]
