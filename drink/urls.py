from django.urls import path, include
from .views import(
    DrinkSerializerListView, 
    DrinkSerializerDetailView, 
    FilterListView,
    WinesAndSpiritsView,
    EnergyDrinksView,
    SoftDrinksView,
    WaterView,
    OrderSerializerView,
    DrinkSerializerListAdminView,
    DrinkSerializerDetailAdminView
) 

urlpatterns = [
    path('', DrinkSerializerListView.as_view()),
    path('control/panel/', DrinkSerializerListAdminView.as_view()),
    path('control/panel/<uuid:pk>', DrinkSerializerDetailAdminView.as_view()),
    path('<uuid:pk>', DrinkSerializerDetailView.as_view()),
    path('energydrinks/', EnergyDrinksView.as_view()),
    path('wines&spirits/', WinesAndSpiritsView.as_view()),
    path('softdrinks/', SoftDrinksView.as_view()),
    path('water/', WaterView.as_view()),
    path('order/', OrderSerializerView.as_view()),
    path('search/', FilterListView.as_view()),
]