from django.apps import AppConfig
from account.utilities import send_activation_notification


class AccountConfig(AppConfig):
    name = 'account'

# user_registered = Signal(providing_args=['instances'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


# user_registered.connect(user_registered_dispatcher)
