from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('blog/type<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),
]