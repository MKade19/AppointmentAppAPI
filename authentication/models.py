from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from employees.models import Employee

class User(AbstractUser):
    email = models.EmailField(unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=-1, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['employee']


    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    verified = models.BooleanField(default=False)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
