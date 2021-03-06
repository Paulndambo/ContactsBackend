from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  country_code = models.CharField(max_length=20)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=200)
  contact_picture = models.URLField(null=True)
  is_favorite = models.BooleanField(default=False)

  def __str__(self):
    return self.owner.username
