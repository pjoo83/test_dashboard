from django.db import models

# Create your models here.

"""
 用户表
"""
IS_IT_EFFECTIVE3 = (
    ('YES', '是'),
    ('NO', '否'),
)


class test_user(models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=30, verbose_name='密码')
    email = models.EmailField(max_length=40, verbose_name='邮箱',null=True, blank=True)
    createTime = models.DateTimeField(max_length=100, auto_now_add=True, null=True, verbose_name="创建时间", blank=True)
    updateTime = models.DateTimeField(auto_now=True, verbose_name="修改时间", null=True, blank=True)
    yn = models.CharField(max_length=100, blank="是否有效", choices=IS_IT_EFFECTIVE3)