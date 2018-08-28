from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
     # ex: /projects/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /project/5/
    path('<int:project_id>/', views.detail, name='detail'),
]