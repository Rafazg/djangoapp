from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .models import Employee, Livros
from .forms import InsereLivroForm
from .forms import RegistrationForm
import requests

# Create your views here.
class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})
        


class Register(View):
    def get(self, request):
        # Lógica para lidar com solicitações GET, como exibir o formulário de registro.
        form = RegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        # Lógica para lidar com solicitações POST, como processar o formulário de registro.
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "register.html", {"form": form})
     

class Index(View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        employees = Employee.objects.all()
        livros = Livros.objects.all()
        livros_encontrados = None

        context = {
            'employees': employees,
            'livros': livros,
            'livros_encontrados': livros_encontrados,
        }

        return render(request, self.template, context)

    def post(self, request):
        livros = Livros.objects.all()
        form = InsereLivroForm(request.POST)  # Use the appropriate form

        if form.is_valid():
            form.save()  # Save the book to the database

        
        if 'search' in request.POST:
            search = request.POST['search']
            chave_api = 'AIzaSyD9jCyxNVQOHpVqN21JaAnQugxh43Wijwo'  # Replace with your actual API key
            
            # Perform the book search
            livros_encontrados = buscar_livros_google_books(search, chave_api)
            print(livros_encontrados)

        context = {
            'livros': livros,
            'form': form,
            'livros_encontrados': livros_encontrados,
        }

        return render(request, self.template, context)        
    
    

class Registrar_Livros(View):
    template_name = 'registrar_livros.html'

    def get(self, request):
        livros = Livros.objects.all()
        form = InsereLivroForm()
        return render(request, self.template_name, {'form': form, 'livros': livros})

    def post(self, request):
        form = InsereLivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
        return render(request, 'index.html', {'form': form})
    
def buscar_livros_google_books(titulo, chave_api):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo}&key={chave_api}"
    response = requests.get(url)
    if response.status_code == 200:
        dados_livros = response.json()
        if "items" in dados_livros:
            livros = dados_livros["items"]
            return livros
    return None
        