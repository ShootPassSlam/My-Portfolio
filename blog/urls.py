from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
     # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/5/
    path('<int:post_id>/', views.detail, name='detail'),
]