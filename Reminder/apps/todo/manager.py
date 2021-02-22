from datetime import datetime

import pytz
from django.db import models


class TaskManager(models.Manager):
    def due_tasks(self):
        cmp = pytz.utc.localize(datetime.now())
        qs = self.get_queryset()
        qs = qs.exclude(due_date__gt=cmp)
        return qs


class CategoryManager(models.Manager):
    def emp_cat(self):
        qs = self.get_queryset()
        qs = qs.filter(task=None)
        return qs
