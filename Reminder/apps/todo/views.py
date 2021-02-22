import mimetypes

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from apps.todo.forms import TaskForm, CategoryForm
from apps.todo.models.todo import Task, Category


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class CategoryList(ListView):
    model = Category


def category_detail(request, category_id):
    category = Task.objects.filter(category=category_id)
    return render(request, 'todo/category_detail.html', {'category': category})


class TaskView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'todo/add_task.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'todo/add_task.html', {'form': TaskForm()})


class CategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'todo/add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'todo/add_category.html', {'form': CategoryForm()})


def d_tasks(request):
    t = Task.objects.due_tasks()
    return render(request, 'todo/d_tasks.html', {'t': t})


def empty_cat(request):
    c = Category.objects.emp_cat()
    return render(request, 'todo/empty_categories.html', {'c': c})


def task_view(request):
    serialized_task_list = serialize('json', Task.objects.all())
    with open('task_list.txt', 'w') as f:
        f.write(serialized_task_list)

    fl_path = r"task_list.txt"
    filename = 'downloaded_task_list.txt'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
