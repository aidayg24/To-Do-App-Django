from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField

from apps.todo.manager import TaskManager, CategoryManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = CategoryManager()

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=timezone.now())
    order = models.CharField(max_length=4)
    status = models.BooleanField(default=False)  # when the user done the task it returns to true
    slug = AutoSlugField(populate_from=['title'], unique=True)

    objects = TaskManager()

    class Meta:
        ordering = ["-due_date"]  # ordering by the due_date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=(str(self.id)))
