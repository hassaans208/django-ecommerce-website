from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=True, widget=forms.TextInput(
        attrs={
            'class': 'block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0 focus:border-primary placeholder-gray-400',
            'placeholder': 'john@example.com'
            }
    ))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0 focus:border-primary placeholder-gray-400',
            'placeholder': 'Please Enter Your Password'
            }
    ))
    remember_me = forms.BooleanField(label="Remember Me", required=False ,widget=forms.CheckboxInput(
        attrs={
            'class': 'text-primary focus:ring-0 rounded-sm cursor-pointer'
        }
    ))