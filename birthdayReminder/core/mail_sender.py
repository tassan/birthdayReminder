from django.core.mail import send_mail


def send_birthday_mail(subject, from_email, to_email, message, html_message: bool):
    send_mail(subject, message, from_email, to_email, html_message=html_message)

