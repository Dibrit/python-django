from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from reg.models import User
from celery import shared_task



@shared_task()
def send_mail_all(text1, text2):
    try:
        for user in User.objects.all():
            send_mail(
                text1,
                text2,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
        print("suc")
    except:
        print('fail')


@shared_task()
def send_mail_personal(user_id, text1, text2):
     UserModel = get_user_model()
     try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            text1,
            text2,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        print('suc')
     except UserModel.DoesNotExist:
         print('fail')


@shared_task()
def email(x):
    print("sfgkijh")
    return x

