from django import forms

from apps.todo.models.todo import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title',
                  'content',
                  'category',
                  'order',
                  'due_date'
                  ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
