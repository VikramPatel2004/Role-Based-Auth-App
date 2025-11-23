from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("create/", views.create_blog, name="create_blog"),
    path("my-blogs/", views.doctor_my_blogs, name="doctor_my_blogs"),
    path("view/", views.view_blogs, name="view_blogs"),
    path("edit/<int:post_id>/", views.edit_blog, name="edit_blog"),
    path("delete/<int:post_id>/", views.delete_blog, name="delete_blog"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),


]
