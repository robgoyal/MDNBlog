from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='index'),
    path('blog/blogs/', views.blogs, name='blogs'),
    path('blog/blogger/<int:author_id>', views.blogger, name='blogger'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
    path('blog/bloggers', views.bloggers, name='bloggers'),
]
