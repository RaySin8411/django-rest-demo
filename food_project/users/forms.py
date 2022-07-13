from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class CustomerUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
