from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, Space 


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
        

class SpaceForm(ModelForm):
    class Meta:
        model = Space
        fields = '__all__'
        exclude = ['host', 'participants']