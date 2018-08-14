from django.shortcuts import render, get_object_or_404
from .models import Lunbo,Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from read_count.utils import read_count_once_read
from comment.models import Comment


each_page_blogs_number = 5


def index(request):
    img_list = Lunbo.objects.filter(chooes=1).order_by('id')
    imgs_list = []
    img_index = []
    for i in img_list:
        if i.chooes==1:
            imgs_list.append(i)
            set(imgs_list)
            list(imgs_list)
    for k,v in enumerate(imgs_list):
        img_index.append(k)

    context ={}
    context['img_list'] = img_list
    context['img_index'] = img_index
    return render(request, 'blog/index.html', context)

def blog_list(request):

    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER)# 每五篇为一页
    page_num = request.GET.get('page', 1)# 获取url的页面参数（get请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2,1),current_page_num)) + list(range(current_page_num,min(current_page_num + 2,paginator.num_pages) + 1))
    if page_range[0] - 1 >= 2:
        page_range.insert(0,"...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")
    # 加首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blog_list.html',context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_count_once_read(request,blog)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type = blog_content_type,object_id=blog.pk)

    context = {}
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    context['blog'] = blog
    context['user'] = request.user
    context['comments'] = comments
    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie(read_cookie_key,'true')
    return response


def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)

    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每五篇为一页
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - 1 >= 2:
        page_range.append("...")
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blog_type']= blog_type

    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()

    return render(request,'blog/blogs_with_type.html',context)