from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User

# class UserManager(BaseUserManager):
#     def create_user(self, userID, password, username=None, phone=None):
#         if not userID:
#             raise ValueError('ID Required')
#
#         user = self.model(userID=userID, username=username, phone=phone)
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, userID, password):
#         user = self.create_user(userID, password)
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     userID = models.CharField(unique=True, max_length=10, verbose_name='아이디')
#     username = models.CharField(max_length=10, null=True, blank=True, verbose_name='유저이름')
#     password = models.CharField(max_length=100, verbose_name='비밀번호')
#     phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='전화번호')
#     pub_date = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'userID'
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.username
#
#     def is_staff(self):
#         return self.is_superuser


class Post(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )

    title = models.CharField(max_length=10)
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __int__(self):
        return self.id
