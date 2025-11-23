# from django.core.mail import send_mail
# from .otp_generator import generate_otp as otp_g
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from .models import Otp

# User = get_user_model()

# def send_otp_via_mail(email):
#     """sending otp to use's mail to verify"""
#     subject = 'Email verification mail'
#     otp = otp_g()
#     message = f'your otp is {otp}'
#     email_from = settings.EMAIL_HOST

#     send_mail(subject, message, email_from, [email])
#     user_obj = Otp.objects.get(user=)
