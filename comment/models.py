from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    text = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add = True,verbose_name='评论时间')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='用户名')

    class Meta:
        ordering = ['-comment_time']