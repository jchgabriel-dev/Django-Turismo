from django.urls import path

from . import views

urlpatterns = [
	path('mainPage', views.mainPage, name='mainPage'),
    path('addPlace', views.addPlace, name='addPlace'),
    path('updatePlace/<int:theid>/', views.updatePlace, name='updatePlace'),
    path('deletePlace/<int:theid>/', views.deletePlace, name='deletePlace'),
]

