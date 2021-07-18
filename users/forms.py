# Django
from django import forms

# Models
from users.models import Profile

class ProfileForm(forms.ModelForm):
    # Model form del Profile
    class Meta:
        # Configuración del Form
        model = Profile
        fields = ("name", "email", "age", "job_title", "company_name")