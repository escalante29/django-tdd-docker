# app/movies/urls.py

# from rest_framework.routers import DefaultRouter

# from .views import MovieViewSet

# router = DefaultRouter()

# router.register(prefix=r"api/movies", viewset=MovieViewSet, basename="movie")

# urlpatterns = router.urls

# # app/movies/urls.py

from django.urls import path

from .views import MovieDetail, MovieList

urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view()),
]
