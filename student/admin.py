from django.contrib import admin
from .models import JoinClass, CommentMain, StudnetWork, ReplyComment

# Register your models here.


@admin.register(JoinClass)
class JoinClassadmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(CommentMain)
class CommentMainadmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(StudnetWork)
class StudnetWorkadmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ReplyComment)
class ReplyCommentadmin(admin.ModelAdmin):
    list_display = ['id']
