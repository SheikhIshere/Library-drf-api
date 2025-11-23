
"""manager file to make code clean and keep stuffs separated """

from django.contrib.auth.models import UserManager


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
