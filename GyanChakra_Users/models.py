from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import GyanChakraUserManager


class GyanChakraUserModel(AbstractUser):
    username=None
    email=models.EmailField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    profession = models.CharField()
    phone = models.CharField()
    address = models.TextField()
    facebook_id_link = models.URLField()
    admin_approval = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','facebook_id_link'] 

    objects = GyanChakraUserManager()

    def __str__(self): 
        return self.email