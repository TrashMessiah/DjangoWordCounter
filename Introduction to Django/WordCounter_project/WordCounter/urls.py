from django.urls import path
from . import views

urlpatterns = [
    #map the route to the view to render and it assigned function together with a name
    #name can be assigned to store a naming to utilize in template independent of whatever we change in here
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about')
]
