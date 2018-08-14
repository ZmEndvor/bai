from django.contrib.auth.models import User
from django.db import models
from django.db.models import SmallIntegerField
from ckeditor_uploader.fields import RichTextUploadingField
from read_count.models import ReadNumExpandMethod


class Lunbo(models.Model):
    IS_CHOOES = (
        (1,'显示到主页'),
        (0,'不显示到主页')
    )
    img = models.ImageField(upload_to="blog", verbose_name='上传图片')
    text = RichTextUploadingField(verbose_name='图片文字',default=' ')
    chooes = SmallIntegerField(choices=IS_CHOOES, verbose_name='图片是否显示在主页')

    class Meta:
        verbose_name = '主页图片展示'
        verbose_name_plural = verbose_name


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return "<Blog:%s>" % self.title

    class Meta:
        ordering = ['-create_time']
