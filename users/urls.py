from django.urls import path
from .views import UserSerializerListView, CustomAuthToken

urlpatterns = [
    path('', UserSerializerListView.as_view()),
    path('token-auth/', CustomAuthToken.as_view()),
]