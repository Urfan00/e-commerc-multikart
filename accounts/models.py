from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField(upload_to = 'users_avatars', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Shipping_address(models.Model):
    company_name = models.CharField(max_length = 100)
    address = models.CharField(max_length= 150)
    postal_code = models.CharField(max_length=5)
    Country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    region_state = models.CharField(max_length=150)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null= True)

    def __str__(self):
        return self.company_name


class Personal_detail(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length= 13)
    message = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null= True)

    def __str__(self):
        return self.first_name
