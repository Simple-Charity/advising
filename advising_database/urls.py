from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    path('', include("analyst.urls")),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)