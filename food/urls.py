from django.urls import path
from .views import *

app_name = 'food'
urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('details/<int:pk>/', FoodDetailView.as_view(), name='details'),
    path('create', FoodCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', FoodUpdateView.as_view(), name='edit'),
    path('delete/<int:id>/', delete , name='delete'),
]