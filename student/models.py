from django.db import models
from teacher.models import CreateClass, Announcement, AddClassWork
from mainapp.models import Student
from django.contrib.auth.models import User
# Create your models here.


class JoinClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    myclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)


class CommentMain(models.Model):
    annoucemain = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    mystu = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=1, blank=True, null=True)
    myteach = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class ReplyComment(models.Model):
    annoucemain = models.ForeignKey(CommentMain, on_delete=models.CASCADE)
    text = models.CharField(max_length=400, default="new")


class StudnetWork(models.Model):
    mystu = models.ForeignKey(Student, on_delete=models.CASCADE)
    mywork = models.ForeignKey(AddClassWork, on_delete=models.CASCADE)
    work = models.FileField(upload_to='images/')
