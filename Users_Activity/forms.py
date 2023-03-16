from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    First_Name = forms.CharField(max_length=100 ,required=True)
    Last_Name = forms.CharField(max_length=50 , required=True)

    class Meta:
        model = User
        fields = ["First_Name" , "Last_Name", "username" , "email" , "password1", "password2"]
        
    def save(self , commit = True):
        user  = super(NewUserForm, self).save(commit=False) #Over ridden save method from UserCreationForm
        user.email  =self.cleaned_data['email']
        user.First_Name = self.cleaned_data['First_Name']
        user.Last_Name = self.cleaned_data['Last_Name']
        if commit:
            user.save()
        return user


    

