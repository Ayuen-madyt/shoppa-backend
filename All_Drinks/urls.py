from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_drinks/', include('drink.urls')),
    path('featured/products/', include('featured.urls')),
    path('banners/', include('banners.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/users/', include('users.urls')),
    path('ordersanditems/', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
