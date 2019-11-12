from django.urls import path
from ex import views

urlpatterns = [
    path('', views.home),
    path('connexion/', views.connetion),
	path('inscription/', views.inscription),
	path('logout/', views.logout),
]
