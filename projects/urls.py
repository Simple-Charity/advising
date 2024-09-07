from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_index, name='site-projects-index'),
    path('<pid>/', views.projects_entry, name='site-projects-entry'),
]
 