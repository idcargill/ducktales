from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Reporter(models.Model):
  name = models.CharField(max_length=60)
  email = models.EmailField()

  def __str__(self):
    return self.name


class Species(models.TextChoices):
  INDIAN_RUNNER   = 'Indian Runner Duck'
  MALLARD         = 'Mallard Duck'
  PEKIN           = 'Pekin Duck'
  KHAKI_CAMPBELL  = 'Khaki Campbell'
  BUFF            = 'Buff'
  MAGPIE          = 'Magpie'

class DuckModel(models.Model):
  name        = models.CharField(max_length=60)
  species     = models.CharField(choices=Species.choices, max_length=30)
  is_laying   = models.BooleanField(default=False)
  age         = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])
  notes       = models.TextField(default='')
  owner       = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  src         = models.CharField(default=f'{species}.jpeg', max_length=30)

  def __str__(self):
    return f'$ID: {self.id}, Duck: {self.name} | Owner: {self.owner}'

  def get_absolute_url(self):
      return reverse("duck_detail", args=[str(self.pk)])

  def get_image_string(self):
      return f'{self.species}.jpeg'