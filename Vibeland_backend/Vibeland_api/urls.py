from django.urls import path, include
from Vibeland_api import views
from Vibeland_api.spotify.authorization import AuthURL, IsAuthenticated, spotifyCallback

#Define the names of the routes to the app's views and endpoints
urlpatterns = [
    path('', views.index, name='index'),
    path('getSpotifyAuthURL', AuthURL.as_view()),
    path('spotifyCallbackRedirect', spotifyCallback),
    path('isSpotifyAuthenticated', IsAuthenticated.as_view()),
    path('spotifyDevAccess/', views.initializeDeveloperAccess, name="developerAccessHandler"),
    path('accessRecommendationSystem/', views.accessRecommendationSystem, name="spotifyVibelandRecSystem")
]