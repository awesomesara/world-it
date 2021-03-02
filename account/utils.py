from django.core.mail import send_mail


def send_activation_mail(user):
    user.create_activation_code()
    message = f"""Спасибо за регистрацию. Активируйте свой аккаунт по ссылке:
    http://127.0.0.1:8000/accounts/activation/?u={user.activation_code}"""
    send_mail(
        'Активация аккаунта',
        message,
        'it-world@my_project.com',
        [user.email, ])