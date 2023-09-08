from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login , name='login' ),
    path('after_login/', views.after_login , name='after_login'),
    path('logout/', views.logout, name="logout"),
]
