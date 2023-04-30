from django.urls import path
from . import views

# 127.0.0.1:8000/movies
# 127.0.0.1:8000/movies/2
# 127.0.0.1:8000/detail
urlpatterns = [
    path('movies',views.index, name='movies'),
    path('<int:movie_id>',views.detail, name='details'),
    path('search',views.search, name='search'),
]