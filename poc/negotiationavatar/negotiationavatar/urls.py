from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('avatar', include('avatar.urls')),
    path('negotiation', include('negotiation.urls')),
    path('summary', include('summary.urls')),
    path('dashboard/', views.dashboard),
    path('', views.dashboard)
]


urlpatterns += staticfiles_urlpatterns()