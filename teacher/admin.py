from pydoc import visiblename
from pyexpat import model
from django.contrib import admin
from .models import CreateClass, Announcement, AddClassWork, QuesModel, ViewCourse, AddCourse, JoinClassteach
# Register your models here.


@admin.register(CreateClass)
class CreateAdmin(admin.ModelAdmin):
    list_display = ['id', "class_code_name", "section", "subject_name"]


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(AddClassWork)
class AddClassWorkAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(AddCourse)
class AddCourseAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'ans']


class MyModelInline(admin.StackedInline):
    model = AddCourse
    extra: 6


@admin.register(ViewCourse)
class OtherModelAdmin(admin.ModelAdmin):
    inlines = [MyModelInline]


@admin.register(JoinClassteach)
class JoinClassteachAdmin(admin.ModelAdmin):
    list_display = ['id']
