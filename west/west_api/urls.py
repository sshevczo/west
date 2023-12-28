from django.urls import path
from .views import item_views, index

urlpatterns = [
    path('', index, name='index'),
    path('item/', item_views, name='item'),

]
