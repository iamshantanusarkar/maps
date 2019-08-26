from django.urls import path
from django.conf.urls import include, url

from api.admin.customer.views import CustomerListCreate, CustomerRetrieveUpdateDestroy
from api.admin.savedmap.views import SavedMapListCreate, SavedMapRetrieveUpdateDestroy
from api.admin.favourte.views import FavouriteListCreate, FavouriteRetrieveUpdateDestroy

urlpatterns = [    
    path('customer', CustomerListCreate.as_view()),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view()),

    path('map', SavedMapListCreate.as_view()),
    path('map/<int:pk>/', SavedMapRetrieveUpdateDestroy.as_view()),

    path('favourite', FavouriteListCreate.as_view()),
    path('favourite/<int:pk>/', FavouriteRetrieveUpdateDestroy.as_view()),
]