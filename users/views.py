# Django
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

# Forms
from users.forms import ProfileForm

# Models
from users.models import Profile

class UserListView(ListView):

    template_name = "list.html"
    model = Profile
    ordering = ("id")
    paginate_by = 1000
    context_object_name = "users"


class UserAddView(CreateView):

    template_name = 'add.html'
    form_class = ProfileForm

    def get_success_url(self):
        # Redirecciona a la vista para listar los usuarios
        return reverse_lazy("users:list")

class UserDetailView(DetailView, UpdateView):
    template_name = "detail.html"
    slug_field = "username"
    slug_url_kwarg = "user"
    queryset = Profile.objects.all()
    context_object_name = "user"
    model = Profile
    fields = ["name", "email", "age", "job_title", "company_name"]
    
    def get_success_url(self):
        # Retorna la página del perfil de usuario
        return reverse('users:list')

def delete_user(request):
    if request.method =="POST":
        my_profile = Profile.objects.get(pk=request.POST.get("profile_pk"))
        my_profile.delete()
        return redirect("users:list")
    return redirect("users:list")
