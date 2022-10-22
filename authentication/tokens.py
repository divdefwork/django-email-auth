""" File description """
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    """
    Тепер кожного разу, коли користувач хоче зареєструватися,
    за допомогою цього класу буде негайно створено унікальний маркер,
    який використовується для створення посилання з нашим доменним іменем,
    і буде надіслано на електронну пошту користувача.
    """
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )
