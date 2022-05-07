from contextlib import nullcontext
from pyexpat import model

from requests import NullHandler
from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Diary(models.Model):
  # Diary model

  user = models.ForeignKey(CustomUser, verbose_name='ユーザ', on_delete=models.PROTECT)
  title = models.CharField(verbose_name='タイトル', max_length=40)
  content = models.TextField(verbose_name='本文', blank=True, null=True)
  photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
  photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
  photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
  created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Diary'

def __str__(self):
    return self.title
