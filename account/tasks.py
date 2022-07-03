from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from account.serializer import UserSerializer
from celery import Celery
app = Celery('tasks', broker='redis://guest@localhost//')


@app.task()
def send_mail_all(text1, text2):
    UserModel = get_user_model()
    try:
        a = UserSerializer.objects.values_list("id")
        for i in a:
            user = UserModel.objects.get(pk=i)
            send_mail(
                text1,
                text2,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
        print("suc")
    except:
        print('fa')


@app.task()
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
         logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
         print('fa')


@app.task()
def email(x):
     return UserSerializer.objects.filter(email=x)

