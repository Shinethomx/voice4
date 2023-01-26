from django import forms

from vfapp.models import MyUser

from django.contrib.auth.forms import UserCreationForm

from vfapp.models import Posts

#                                                               registration form !!!!!!

class RegistrationForm(UserCreationForm):
    class Meta():

        model=MyUser

        fields=[

            "first_name",
            'last_name',
            'username',
            'email',
            'phone',
            'profile_pic',
            'password1',
            'password2'
            
            ]
#                                                                login form!!!!!!!!!


class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

#                                                               post form!!!!!!!!!

class PostForm(forms.ModelForm):

    class Meta:

        model=Posts
        fields=[

            "image",
            "caption",
            "video",

        ]
        widgets={
          
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "video":forms.FileInput(attrs={"class":"form-control"}),
            "caption":forms.Textarea(attrs={"class":"form-control","placeholder":"caption","rows":3})

        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=['username','email']