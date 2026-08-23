from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):

    EDUCATION_CHOICES = [
        ('HSC', 'HSC'),
        ('UG', 'Undergraduate (UG)'),
        ('PG', 'Postgraduate (PG)'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    full_name = models.CharField(max_length=150)

    education_level = models.CharField(
        max_length=10,
        choices=EDUCATION_CHOICES
    )

    preferred_institute = models.CharField(
        max_length=200
    )

    career_interest = models.CharField(
        max_length=150
    )

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return self.full_name