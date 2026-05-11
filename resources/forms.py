from django import forms
from .models import Resource, ResourceRequest, RequestBoardPost, UserProfile
from django.contrib.auth.models import User

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'category', 'condition', 'image', 'action_type', 'price']
    
    def clean(self):
        cleaned_data = super().clean()
        action_type = cleaned_data.get('action_type')
        price = cleaned_data.get('price')
        
        if action_type == 'Sell' and not price:
            raise forms.ValidationError("Price is required when selling a resource.")
        
        if action_type != 'Sell' and price:
            cleaned_data['price'] = None  # Clear price if not selling
            
        return cleaned_data

class ResourceRequestForm(forms.ModelForm):
    class Meta:
        model = ResourceRequest
        fields = ['message']

class RequestBoardPostForm(forms.ModelForm):
    class Meta:
        model = RequestBoardPost
        fields = ['title', 'description']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['year', 'branch', 'college']

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 