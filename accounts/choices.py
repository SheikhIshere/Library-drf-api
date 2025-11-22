from django.db import models


"""helper function to support main """

class SubscriptionPlan(models.TextChoices):
    """subscription plan for user who is using"""
    FREE = 'free', 'Free'
    GOLD = 'gold', 'Gold'
    DIAMOND = 'diamond', 'Diamond'