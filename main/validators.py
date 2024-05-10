

from django.core.exceptions import ValidationError
import re


def check_phone_number(user_tel):
    number = user_tel
    if re.match(r'^(\+375|375|80)?[\s\-]?[0-9]{2}?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', number):
        print('NumberTrue')
        return
    else:
        print('NumberFalse')
        print(user_tel)
        raise ValidationError('Неверный формат номера')
