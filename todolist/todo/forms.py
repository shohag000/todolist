from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class UserLoginForm(forms.Form):
    email= forms.CharField(label="Email",widget=forms.TextInput(
        attrs={
            "class" : "form-control",
            "placeholder" : "Enter email",
        }
    ))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter password",
        }
    ))


    def clean(self,*args,**kwargs):
        email= self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = User.objects.get(email__iexact=email)
        if not user.check_password(password):
            raise forms.ValidationError("Password incorrect")
        self.cleaned_data["user"]=user
        return super(UserLoginForm,self).clean(*args,**kwargs)