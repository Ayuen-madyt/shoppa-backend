from django.urls import path
from .views import (
    BannerSerializerView,
    BannerSerializerListAdminView,
    BannerSerializerDetailAdminView
)

urlpatterns = [
    path('', BannerSerializerView.as_view()),
    path('control/panel/', BannerSerializerListAdminView.as_view()),
    path('control/panel/<int:pk>/', BannerSerializerDetailAdminView.as_view()),
]