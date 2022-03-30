from django import forms

class HotelForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    address = forms.CharField(label='address', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    pages_number = forms.IntegerField(label="Pages number")
    number_stars = forms.IntegerField(label='number_stars')
    number_rooms = forms.IntegerField(label='number_rooms')
    description = forms.CharField(label="Description", widget=forms.Textarea)


class EditHotelDescriptionForm(forms.Form):
    description = forms.CharField(label="Description", widget=forms.Textarea)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)