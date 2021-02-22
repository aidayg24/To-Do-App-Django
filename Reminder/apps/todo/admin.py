from django.contrib import admin

from apps.todo.models.todo import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['title',
              'content',
              'category',
              'order',
              'status',
              'due_date'
              ]
    list_display = ['title',
                    'content',
                    'category',
                    'order',
                    'status',
                    'due_date'
                    ]
    search_fields = ['title',
                     'category',
                     'order',
                     'status',
                     'due_date'
                     ]
