from django.urls import path
from toDoApp.views import home_page, view_task, view_past

urlpatterns = [
    path('', home_page, name="home-page"),
    path('task/', view_task, name="current-task"),
    path('past/', view_past, name="completed-task"),
]