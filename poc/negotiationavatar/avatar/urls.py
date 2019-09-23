
from django.urls import path
from .import views

app_name = 'avatar'


urlpatterns = [
    path('', views.home_page),
    path('home/', views.home_page, name="home"),
    path('deals/', views.deals),
    path('register/', views.registration_form),
    path('login/', views.login_form, name="login")
]
