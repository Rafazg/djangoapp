from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name ='register'),
    path('index/', views.Index.as_view(), name='index'),
    path('registrar_livros/', views.Registrar_Livros.as_view(), name='registrar_livros'),
]