from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Введите пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторить пароль")

    username.widget.attrs.update({"class": "form__widget"})
    password.widget.attrs.update({"class": "form__widget"})
    password2.widget.attrs.update({"class": "form__widget"})

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class FilterByPrice(forms.Form):
    choice_form = forms.ChoiceField(choices={'product_properties__pub_date': 'дате добавления',
                                             'product_name': 'названию: «от А до Я»',
                                             '-product_name': 'названию: «от Я до А»',
                                             'product_properties__price': 'цене по возрастанию',
                                             '-product_properties__price': 'цене по убыванию',
                                             'product_properties__rating': 'популярности'})
    choice_form.widget.attrs.update({"class": "form__widget"})


class FilterByBrand(forms.Form):
    brand_form = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Выбрать брэнд',
                                           choices={'1': 'Alleva',
                                                    '2': 'Bon appetit',
                                                    '3': 'Little one',
                                                    '4': 'Purina',
                                                    '5': 'Royal canin',
                                                    '6': 'Versele laga'})
    brand_form.widget.attrs.update({"class": "form__widget"})


class ChangeLoginForm(forms.Form):
    new_login = forms.CharField(label="Новый логин", required=False, help_text='Необязательное поле')
    new_password = forms.CharField(widget=forms.PasswordInput, label="Введите пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")
