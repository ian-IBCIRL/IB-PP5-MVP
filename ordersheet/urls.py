from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordersheet, name='view_ordersheet'),
    path('add/<item_id>/', views.add_to_ordersheet, name='add_to_ordersheet'),
    path('adjust/<item_id>/', views.adjust_ordersheet, name='adjust_ordersheet'),
    path('remove/<item_id>/', views.remove_from_ordersheet, name='remove_from_ordersheet'),  # noqa
]
