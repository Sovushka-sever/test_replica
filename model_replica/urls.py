from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_workers, name='create_workers'),
    path('db/', views.main_db, name='db'),
    path('replica/', views.replica_db, name='replica'),
]
