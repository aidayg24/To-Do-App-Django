
from django.urls import path

from apps.todo import views
from apps.todo.views import TaskList, CategoryList, TaskDetail, category_detail, TaskView, CategoryView, d_tasks, \
    task_view, empty_cat

urlpatterns = [
    path('tasks/', TaskList.as_view(), name="list_of_tasks"),
    path('<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('categories/', CategoryList.as_view(), name="list_of_categories"),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('due/', d_tasks, name='d_tasks'),
    path('emp/', empty_cat, name='emp_cat'),
    path('addtasks/', TaskView.as_view(), name="add_new_task"),
    path('addcategory/', CategoryView.as_view(), name="add_new_category"),
    path('taskdownload/', task_view, name='task_view'),

]
