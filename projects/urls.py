from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
     # ex: /projects/
    path('', views.index, name='index'),
    # ex: /project/3/
    path('<int:project_id>/', views.detail, name='detail'),
]