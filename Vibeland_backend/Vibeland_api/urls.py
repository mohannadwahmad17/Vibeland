from django.urls import path, include
from Vibeland_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spotifyDevAccess/', views.initializeDeveloperAccess, name="developerAccessHandler"),
    path('accessRecommendationSystem/', views.accessRecommendationSystem, name="spotifyVibelandRecSystem")
]