from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from .models import Comment
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def update_comment(request):
    user = request.user
    text = request.POST.get('comment_text').strip()
    if text == '':
        return JsonResponse({'err':0,'msg':'评论内容不能为空'})
    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()


    return JsonResponse({'err':1})