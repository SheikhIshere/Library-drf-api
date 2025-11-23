"""here i am defining the user model"""

from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin,
)
from .manager import AccountManager
from django.db import models
from choices import SubscriptionPlan
from datetime import timezone
from django.utils import timezone



class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model using email as the unique identifier."""
    email = models.EmailField()
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile_img/')
    
    
    subscription_plan = models.CharField(
        max_length=20,
        choices=SubscriptionPlan.choices,
        default=SubscriptionPlan.FREE
    )

    # for authentication and power
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def generate_uniq_username(self):
        """here i am predefining the user name"""
        if self.username:
            return
        
        base = self.email.split('@')[0].lower()
        username = base

        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{counter}"
            counter += 1
        
        self.username = username
    
    # Auto-call this before every save
    def save(self, *args, **kwargs):
        self.generate_unique_username()
        super().save(*args, **kwargs)        



class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    date_created = models.DateTimeField(default=timezone.now())
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.date_created + timezone.timedelta(minutes=5)

    def use(self):
        if self.is_used or self.is_expired:
            self.delete()
            return False
        self.is_used = True
        self.save()
        return True