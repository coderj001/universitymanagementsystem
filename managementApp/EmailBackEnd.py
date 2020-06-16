from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

'''
Setting-Up Custom Authentication To Auth with email and password
'''
class EmailBackEnd(ModelBackend):
    def authenticate(self,username=None, password=None, **kwargs):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None