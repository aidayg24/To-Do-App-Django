from datetime import datetime

import pytz
from django import template
from django.utils.timesince import timesince

from apps.todo.models.todo import Task

register = template.Library()


@register.inclusion_tag('todo/recent_tasks.html')
def t_recent_tasks():
    tasks = Task.objects.all().order_by('-id')[:4]
    return {'tasks': tasks}


@register.simple_tag
def time_duration_tasks(the_time):
    cmp = pytz.utc.localize(datetime.now())
    if the_time > cmp:
        return "%s until this task." %timesince(cmp, the_time)
    else:
        return "This task ended %s ago." % timesince(the_time, cmp)


@register.filter(name='ti')
def ti(value):
    return value.title()
