from django.urls import path
from . import views 
#http://127.0.0.1:8000/


urlpatterns = [
    path('travelpage',views.travelwebpage, name= 'travelwebpage'),
    path('blog',views.blog,name='blog'),
    path('',views.index, name= 'index'),

]