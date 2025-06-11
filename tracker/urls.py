from django.urls import path
from . import views

urlpatterns = [
    path('repositories/create/', views.create_repository, name='create_repository'),
    path('repositories/', views.repository_list, name='repository_list'),
    path('repositories/<int:repo_id>/branches/', views.branch_list, name='branch_list'),
    path('repositories/<int:repo_id>/branches/create/', views.create_branch, name='create_branch'),
    path('branches/<int:branch_id>/commits/', views.commit_list, name='commit_list'),



]
