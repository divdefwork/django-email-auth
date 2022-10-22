from django.core.mail import send_mail
from cryptography.fernet import Fernet
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import TokenGenerator
from django.utils.encoding import force_bytes
from django.apps import apps


def send_activation_mail(**kwargs):
    """
    Функція відповідає за надсилання повідомлення електронної пошти з
    підтвердженням на електронну пошту користувача з посиланням для активації,
    яке генерує наш TokenGeneratorклас.
    """
    # Отримати модель користувача
    UserModel = apps.get_model('authentication', 'User')
    # Отримати призначеного користувача за ідентифікатором користувача
    user = UserModel.objects.get(pk=kwargs['userID'])
    # Створіть об’єкт TokenGenerator
    account_activation_token = TokenGenerator()

    context = {
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # Create activation token and pass it to the HTML template
        'token': account_activation_token.make_token(user)
    }

    html_content = render_to_string('registration/email_confirmation.html',
                                    context)

    mail = {
        'subject': "Електронне підтвердження",
        'message': None,
        'html_message': html_content,
        'from_email': settings.EMAIL_HOST_USER,
    }

    send_mail(**mail, fail_silently=True, recipient_list=[user.email])

    return
