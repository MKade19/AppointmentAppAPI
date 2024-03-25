from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from departments.models import Department
from roles.models import Role

class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phone', 'address', 'department', 'role']

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
