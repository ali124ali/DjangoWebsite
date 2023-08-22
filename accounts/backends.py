# from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.backends import ModelBackend

UserModel = User

class EmailBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        try:
            user = UserModel.objects.get(email=username)
        except:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        UserModel = User

        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None