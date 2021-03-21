from django.urls import path
from.views import (
    FeaturedSerializerListView,
    FeaturedSerializerListAdminView,
    FeaturedSerializerDetailAdminView
)

urlpatterns = [
    path('', FeaturedSerializerListView.as_view()), # client end point readonly
    path('control/panel/', FeaturedSerializerListAdminView.as_view()), # Admin endpoint only
    path('control/panel/<int:pk>', FeaturedSerializerDetailAdminView.as_view()), # Admin endpoint only
]

