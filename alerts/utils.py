from django.core.mail import send_mail


def send_alert_email(message, to):
    try:
        send_mail(
            'Alert CryptoApp',
            message,
            'hello@cryptoapp.com',
            [to],
            fail_silently=False,
        )
    except ConnectionRefusedError:
        pass
