"""

"""
from django.contrib import admin
from django.urls import path
from todo.views import mytodo,update_task
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mytodo, name='mytodo'),
    path('update-task/<int:id>/', update_task, name='update_task'),

    
]
