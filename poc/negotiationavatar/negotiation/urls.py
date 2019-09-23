
from django.urls import path
from .import views
urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard),
    path('keywords/', views.keywords),
    path('commonfactors/', views.common_factors)
]