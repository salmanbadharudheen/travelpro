from django.urls import path
from .import views
urlpatterns=[
    path('data',views.data,name="data"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]