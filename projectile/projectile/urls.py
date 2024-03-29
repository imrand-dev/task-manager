"""
URL configuration for projectile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from drf_spectacular.views import(
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

admin.site.site_header = "Task Management"
admin.site.index_title = "Task Management Dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    # drf session auth
    path("api-auth/", include("rest_framework.urls")),
    # swagger api
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # auth
    path("api/v1/auth", include("accounts.rest.urls")),
    # me
    path("api/v1/me", include("tasks.rest.urls")),
]

if settings.DEBUG:
    debug_toolbar_url = [
        path("__debug__", include("debug_toolbar.urls")),
    ]
    urlpatterns += debug_toolbar_url
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)