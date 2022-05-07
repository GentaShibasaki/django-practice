import csv
import datetime
from lib2to3.pytree import Base
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Diary

class Command(BaseCommand):
  help = 'Backup Diary data'

  def handle(self, *args, **kwargs):
    # get YYYYMMDD at exection time
    date = datetime.date.today().strftime('%Y%m%d')

    # relative path for saving files
    file_path = settings.BACKUP_PATH + 'diary_' + date +'.csv'

    # if backup directory doesn't exist, create it
    os.makedirs(settings.BACKUP_PATH, exist_ok=True)

    # create backup file
    with open(file_path, 'w') as file:
      writer = csv.writer(file)

      # the following syntax is list comprehension. EX:
      # 
      # myList = []
      #   for i in range(10):
      #     myList.append(i)
      # 
      # is equivalent to
      # 
      # myList = [i for i in range(10)]

      header = [field.name for field in Diary._meta.fields]

      diaries = Diary.objects.all()
      for diary in diaries:
        writer.writerow([
          str(diary.user),
          diary.title,
          str(diary.photo1),
          str(diary.photo2),
          str(diary.photo3),
          str(diary.created_at),
          str(diary.updated_at)
        ])

      files = os.listdir(settings.BACKUP_PATH)
      if len(files) >= settings.NUM_SAVED_BACKUP:
        files.sort()
        os.remove(settings.BACKUP_PATH + files[0])





