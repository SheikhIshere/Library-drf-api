"""here i am defining the user model"""

from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.db import models
from choices import SubscriptionPlan
from datetime import timezone


class AccountManager(UserManager):
    """here i will be managing all of the accounts including admin panel"""
    def create_user(self, email, password, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser with staff and superuser privileges."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


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
    is_active = models.BooleanField(default=False)
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