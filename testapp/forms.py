from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from testapp.models import Laptop



class UserRegForm(UserCreationForm):
    # email = forms.EmailField() # converts to html <input type='email'>


    class Meta:
        model = User # specify from which model u r inheriting the fields
        fields = ('first_name','last_name','username','email', 'password1','password2') # specify fields to show to the user

        # others ways of specifying fields to show
        # exclude = ('first_name',) # display all fields except 'firstname'

        # fields = '__all__' # display all the fields

class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = '__all__'