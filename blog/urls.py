from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('post/create/', views.PostCreate.as_view(), name='post_create_url'),
    path('<int:id>/', views.post_detail, name='post_detail'),

]