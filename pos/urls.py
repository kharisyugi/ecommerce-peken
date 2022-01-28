
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('customers/', include('customers.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', include('products.urls')),
    path('sales/', include('sales.urls')),
    path('toko/', include('toko.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('account/password-reset/', include('django_rest_resetpassword.urls', namespace='password_reset')),
    

]
