from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("loguot/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.home, name="home"),
    path("", include("brands.urls")),
    path("", include("categories.urls")),
    path("", include("suppliers.urls")),
    path("", include("inflows.urls")),
    path("", include("outflows.urls")),
    path("", include("products.urls")),

    # API
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
    path('', include('suppliers.urls')),

    path('api/v1/', include('authentication.urls'))
]
