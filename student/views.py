from email import message
from pickle import NONE
from tkinter.messagebox import NO
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

from mainapp.models import Student
from .models import JoinClass, CommentMain, StudnetWork, ReplyComment
from teacher.models import AddClassWork, CreateClass, Announcement, QuesModel, JoinClassteach
# Create your views here.
from django.contrib import messages
from teacher.models import AddCourse, ViewCourse
from .forms import CommentForm
from mainapp.forms import StudentRegisterForm, StudentEditRegisterForm


class StudentHome(View):
    def get(self, request):
        student = request.session.get("student")
        if student:
            studentuser = Student.objects.get(pk=student)
            classview = JoinClass.objects.filter(student=studentuser)
            return render(request, 'student_home.html', {'classview': classview})
        else:
            return redirect("/")


class JoinClassView(View):
    def get(self, request):
        student = request.session.get("student")
        if student:
            allclass = JoinClass.objects.filter()
            return render(request, 'joinclass.html')
        else:
            return redirect("/")

    def post(self, request):
        student = request.session.get("student")
        class_code = request.POST.get("class_code")
        studentuser = Student.objects.get(pk=student)
        try:
            allclass = CreateClass.objects.get(classcode=class_code)
        except:
            allclass = NONE

        classview = JoinClass(student=studentuser, myclass=allclass)

        n = JoinClass.objects.filter(
            student=studentuser, myclass__classcode=class_code)

        if n:
            messages.warning(request, "Class Already Exits")

        else:
            if classview:
                classview.save()
                return redirect("/student")

        return render(request, 'joinclass.html')


class ClassworkView(View):
    def get(self, request, id):
        student = request.session.get("student")
        if student:
            allclass = JoinClass.objects.get(id=id)
            my_class = CreateClass.objects.get(
                classcode=allclass.myclass.classcode)
            annoucement = Announcement.objects.filter(classview=my_class)
            print(my_class)
            return render(request, 'stream.html', {'annoucement': annoucement, 'mainid': id})
        else:
            return redirect("/")


class AnnouceView(View):
    def get(self, request, id):
        student = request.session.get("student")
        if student:

            annoucementview = Announcement.objects.get(id=id)
            comment_view = CommentMain.objects.filter(
                annoucemain=annoucementview)[::-1]

            return render(request, 'anounceview.html', {'annoucementview': annoucementview, 'comment_view': comment_view})

        return render(request, 'anounceview.html', {'annoucementview': annoucementview, 'comment_view': comment_view})

    def post(self, request, id):
        student = request.session.get("student")
        stuenclass = Student.objects.get(pk=student)
        commenttext = request.POST.get("commenttext")
        annoucementview = Announcement.objects.get(id=id)

        savecomment = CommentMain(
            annoucemain=annoucementview, mystu=stuenclass, comment=commenttext)
        savecomment.save()

        comment_view = CommentMain.objects.filter(
            annoucemain=annoucementview)[::-1]
        return render(request, 'anounceview.html', {'annoucementview': annoucementview, 'comment_view': comment_view})


class WorkView(View):
    def get(self, request, id):
        student = request.session.get("student")
        if student:
            allclass = JoinClass.objects.get(id=id)
            my_class = CreateClass.objects.get(
                classcode=allclass.myclass.classcode)
            classwork = AddClassWork.objects.filter(myclass=my_class)
            return render(request, 'work.html', {'classwork': classwork,  'mainid': id})
        return render(request, 'work.html', {'classwork': classwork,  'mainid': id})


class FullWorkView(View):
    def get(self, request, id):
        student = request.session.get("student")
        classwork = AddClassWork.objects.get(id=id)
        try:
            stuwork = StudnetWork.objects.get(mywork=classwork)
        except:
            stuwork = None
        if student:
            return render(request, 'workfullview.html', {'classwork': classwork, 'stuwork': stuwork})

    def post(self, request, id):
        classwork = AddClassWork.objects.get(id=id)

        student = request.session.get("student")
        print(student)
        myfile = request.FILES['myfile']
        classwork = AddClassWork.objects.get(id=id)
        stu = Student.objects.get(id=student)
        allfile = StudnetWork(mystu=stu, mywork=classwork, work=myfile)
        allfile.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FullCourseiew(View):
    def get(self, request):
        student = request.session.get("student")
        coursem = ViewCourse.objects.all()
        if student:
            return render(request, 'viewcoursestu.html',   {'coursem': coursem})


class FullCourseiewfull(View):
    def get(self, request, id):
        student = request.session.get("student")
        course = ViewCourse.objects.get(pk=id)
        detail_view = AddCourse.objects.filter(course=course)
        if student:
            return render(request, 'detailviewcoursestu.html',   {'course': course, 'detail_view': detail_view})


def studentlogout(request):
    try:
        del request.session['student']
    except:
        pass
    return redirect("/")


def deleletwork(request, id):
    print(id)
    myw = StudnetWork.objects.get(id=id)
    myw.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleltecommentstu(request, id):
    comment = CommentMain.objects.get(id=id)
    comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class EditCommentview(View):
    def get(self, request, id):

        mycom = CommentMain.objects.get(pk=id)
        form = CommentForm(instance=mycom)

        return render(request, 'editcomment.html', {'form': form})

    def post(self, request, id):
        student = request.session.get("student")
        mystu = Student.objects.get(pk=student)
        mycom = CommentMain.objects.get(pk=id)
        form = CommentForm(request.POST, instance=mycom)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.mystu = mystu
            obj.annoucemain = mycom.annoucemain

            obj.save()
            messages.success(request, "Successfully Edited")
            return HttpResponseRedirect('/student/annouceview/%d/' % mycom.annoucemain.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def showreplystu(request, id):

    comment = CommentMain.objects.get(id=id)
    allreply = ReplyComment.objects.filter(annoucemain=comment)
    return render(request, 'anounceview.html', {"allreply": allreply})


class EditStudent(View):
    def get(self, request):
        student = request.session.get("student")
        studentst = Student.objects.get(id=student)
        form = StudentEditRegisterForm(instance=studentst)
        if student:
            return render(request, 'update_student.html', {'form': form})

    def post(self, request):
        student = request.session.get("student")
        mystu = Student.objects.get(id=student)

        form = StudentEditRegisterForm(request.POST, instance=mystu)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = mystu.password
            obj.save()
        else:
            return HttpResponse("eror")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletejoinclass(request, id):
    joinclass = JoinClass.objects.get(id=id)
    joinclass.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ExamShowStudent(View):
    def get(self, request, id):
        mywork = JoinClass.objects.get(pk=id)
        exam = QuesModel.objects.filter(myclass=mywork.myclass)[::-1]
        return render(request, "showexamviewstudent.html", {'exam': exam, "mainid": id})


def show_people_work_view_student(request, id):
    joinclass = JoinClass.objects.get(id=id)
    joinclassteacher = JoinClassteach.objects.filter(myclass=joinclass.myclass)
    joinstudent = JoinClass.objects.filter(myclass=joinclass.myclass)
    return render(request, "showstudentpeople.html", {'mainid': id, "joinclassteacher": joinclassteacher, "joinstudent": joinstudent})
