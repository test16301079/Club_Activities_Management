import time
from datetime import timezone

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import re

class Upload(models.Model):
  username = models.CharField(max_length=16)
  avatar = models.FileField(upload_to='avatar')


class MyUserManager(BaseUserManager):
    def create_user(self, email, created_at, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            created_at=created_at,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,created_at, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            created_at=created_at,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=40,
        unique=True,
    )
    username = models.CharField(
        max_length=40,
        primary_key=True
    )
    created_at = models.DateField()

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['created_at']

    def __str__(self):
        return self.email


class Activities(models.Model):
    activityid = models.AutoField(primary_key=True)
    activityname = models.CharField(max_length=40)
    activitytype = models.IntegerField(default=0, choices=((0, '学术类'), (1, '体育类'), (2, '科技类'), (3, '文化类')))
    activitytime = models.DateTimeField()
    activitycapacity = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(40),
            MinValueValidator(1)
        ])
    openenrolltime = models.DateTimeField()

class Enrollment(models.Model):
    username = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    activityid = models.ForeignKey('Activities', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)



class Oldperson(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    id_card = models.CharField(max_length=50, default='')
    birthday = models.DateTimeField()
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    #图像目录
    imgset_dir = models.CharField(max_length=200, default='')
    #头像路径
    profile_photo = models.CharField(max_length=200, default='')
    room_number = models.CharField(max_length=50, default='')
    firstguardian_name = models.CharField(max_length=50, default='')
    firstguardian_relationship = models.CharField(max_length=50, default='')
    firstguardian_phone = models.CharField(max_length=50, default='')
    firstguardian_wechat = models.CharField(max_length=50, default='')
    secondguardian_name = models.CharField(max_length=50, default='')
    secondguardian_relationship = models.CharField(max_length=50, default='')
    secondguardian_phone = models.CharField(max_length=50, default='')
    secondguardian_wechat = models.CharField(max_length=50, default='')

    health_state = models.CharField(max_length=50, default='')
    DESCRIPTION = models.CharField(max_length=200,default='')
    is_active = models.BooleanField(default=True)

    created_at = models.DateField()
    created_by = models.ForeignKey('MyUser', on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['created_at']



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,default='')
    gender = models.IntegerField(default=0, choices=((0, '男'), (1, '女')))
    phone = models.CharField(max_length=50,default='')
    id_card = models.CharField(max_length=50,default='')
    birthday = models.DateTimeField()
    hire_date = models.DateTimeField()
    resign_date = models.DateTimeField()
    #图像目录
    imgset_dir = models.CharField(max_length=200,default='')
    #头像路径
    profile_photo = models.CharField(max_length=200,default='')
    DESCRIPTION = models.CharField(max_length=200,default='')
    ISACTIVE = models.CharField(max_length=10, default='有效')
    # CREATED = models.DateTimeField(null=True, blank=True)
    CREATEBY = models.ForeignKey('MyUser', on_delete=models.CASCADE, null=True, related_name="create_user")
    # UPDATED = models.DateTimeField(null=True, blank=True)
    UPDATEBY = models.ForeignKey('MyUser', on_delete=models.CASCADE, null=True, related_name="update_user")


