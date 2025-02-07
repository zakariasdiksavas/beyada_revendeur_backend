from django.urls import path
from .views import *

urlpatterns = [
    path('create-personnel', create_personnel),
    path('update-personnel', update_personnel),
    path('delete-personnel', delete_personnel),
    path('list-personnel', list_personnel),

    path('create-maindoeuvre', create_maindoeuvre),
    path('update-maindoeuvre', update_maindoeuvre),
    path('delete-maindoeuvre', delete_maindoeuvre),
    path('list-maindoeuvre', list_maindoeuvre),

    path('create-transport', create_transport),
    path('update-transport', update_transport),
    path('delete-transport', delete_transport),
    path('list-transport', list_transport),
    
    path('create-category', create_category),
    path('update-category', update_category),
    path('delete-category', delete_category),
    path('list-category', list_category),

    path('create-divers', create_divers),
    path('update-divers', update_divers),
    path('delete-divers', delete_divers),
    path('list-divers', list_divers),
]