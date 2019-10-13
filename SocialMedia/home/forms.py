from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profile,ImagePost




class UserForm(UserCreationForm):
    name =forms.CharField(max_length=50)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')
    image = forms.ImageField(required=False, label='ProfilePic:(optional)')
    class meta:
        model = User
        fields =['name','email','phone','password1','password2','image']

class EditProfile(UserChangeForm):
    class Meta:
        model=Profile
        fields=['name', 'email','phone']



# class PostForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields=['title','text']


class ImagePostForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        fields = ['title', 'cover']