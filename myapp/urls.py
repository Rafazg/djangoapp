from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name ='register'),
    path('index/', views.Index.as_view(), name='index'),
    path('registrar_livros/', views.Registrar_Livros.as_view(), name='registrar_livros'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)