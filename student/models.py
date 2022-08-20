from django.db import models
from teacher.models import CreateClass, Announcement, AddClassWork
from mainapp.models import Student

# Create your models here.


class JoinClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    myclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)


class CommentMain(models.Model):
    annoucemain = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    mystu = models.ForeignKey(Student, on_delete=models.CASCADE)
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
