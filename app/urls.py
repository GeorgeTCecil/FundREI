from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('reg_process', views.registration),
    path('login_process', views.login),
    # path('project/new', views.add_project),
    path('new_project', views.new_project),
    path('add-project/', views.image_upload_view),
    path('project/<int:id>', views.this_project),
    path('portfolio/<user_id>', views.portfolio),
    path('add_inv/<user_id>/<project_id>', views.add_inv),
    path('investments/<user_id>', views.my_inv),
    path('project/edit/<int:id>', views.edit_project),
    path('project/<int:id>/remove', views.destroy),
    path('project/<int:id>/investors', views.projinv),
]