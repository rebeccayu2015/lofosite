from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_missing/', views.add_missing, name='add_missing'),
    path('missing_list/', views.missing_list, name='missing_list'),
]
