from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  # Argumented user model

  class Meta:
    verbose_name_plural = 'CustomUser'
