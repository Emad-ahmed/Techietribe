from ast import Return
from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views import View

from mainapp.forms import SignForm
from .models import CreateClass, Announcement, AddClassWork, QuesModel, AddCourse, ViewCourse
from .forms import AnnouncementForm, CreateClassForm, AddClassWorkForm, MyPasswordChangeForm, QuesModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

from teacher.forms import ViewCourseForm, AddlinkForm
from student.models import CommentMain, Student, ReplyComment


class TeacherHome(View):
    def get(self, request):
        if request.user.is_authenticated:
            create = CreateClass.objects.filter(user=request.user)
            return render(request, 'teacher_home.html', {'create': create})
        else:
            return redirect("/")


class CreateClassview(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = CreateClassForm()
            return render(request, 'createclass.html', {'form': fm})
        else:
            return redirect("/")

    def post(self, request):
        fm = CreateClassForm(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Successfully Saved")
        else:
            messages.warning(request, "Failed To Saved")
        return render(request, 'createclass.html', {'form': fm})


class ClassShow(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            mainid = id
            classshow = CreateClass.objects.get(pk=id)
            allannouce = Announcement.objects.filter(classview=classshow)[::-1]
            return render(request, 'classview.html', {'classshow': classshow, "mainid": mainid, 'allannouce': allannouce})
        else:
            return redirect("/")

    def post(self, request, id):
        mainid = id
        classshow = CreateClass.objects.get(pk=id)

        myuser = request.user
        annouce = request.POST.get("annouce")
        print(annouce)
        annoucesave = Announcement(
            user=myuser, classview=classshow, text=annouce)
        annoucesave.save()
        messages.success(request, "Successfully Saved")
        allannouce = Announcement.objects.filter(classview=classshow)[::-1]
        return render(request, 'classview.html', {'classshow': classshow, "mainid": mainid,  'allannouce': allannouce})


class AnnView(View):
    def get(self, request, id):
        mainid = id
        if request.user:
            annoucementview = Announcement.objects.get(id=id)
            comment_view = CommentMain.objects.filter(
                annoucemain=annoucementview)[::-1]
            replycomment = ReplyComment.objects.filter(
                annoucemain__annoucemain=annoucementview)
            print(replycomment)
            return render(request, 'annview.html', {'annoucementview': annoucementview, 'comment_view': comment_view, "replycomment": replycomment, 'mainid': mainid})

        return render(request, 'annview.html', {'annoucementview': annoucementview, 'comment_view': comment_view, "replycomment": replycomment, 'mainid': mainid})


def userlogout(request):
    logout(request)
    return redirect('/')


def deletecard(request, id):
    crea = CreateClass.objects.get(pk=id)
    crea.delete()
    messages.warning(request, "Successfully Deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletelist(request, id):
    ann = Announcement.objects.get(pk=id)
    ann.delete()
    messages.warning(request, "Successfully Deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletework(request, id):
    ann = AddClassWork.objects.get(pk=id)
    ann.delete()
    messages.warning(request, "Successfully Deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class Addworkview(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            mainid = id
            classshow = CreateClass.objects.get(pk=id)
            allwork = AddClassWork.objects.filter(myclass=classshow)[::-1]
            fm = AddClassWorkForm()
            return render(request, 'add_work.html', {'form': fm, "mainid": mainid,  'allwork': allwork})
        else:
            return redirect("/")

    def post(self, request, id):
        mainid = id
        fm = AddClassWorkForm(request.POST, request.FILES)

        classv = CreateClass.objects.get(pk=id)

        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.myclass = classv
            obj.save()
            messages.success(request, "Successfully Saved")
        else:
            messages.warning(request, "Failed To Saved")
        allwork = AddClassWork.objects.filter(myclass=classv)[::-1]
        return render(request, 'add_work.html', {'form': fm, "mainid": mainid,   "allwork": allwork})


class ShowWorkview(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            allwork = AddClassWork.objects.get(pk=id)
            return render(request, 'ShowWork.html', {'allwork': allwork})
        else:
            return redirect("/")


class PasswordChangeView(View):
    def get(self, request):
        form = MyPasswordChangeForm(user=request.user)

        return render(request, 'passwordchange.html', {'form': form})

    def post(self, request):
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return redirect("/")
        else:
            messages.error(request, "Please Enter Valid Password")
            return render(request, 'passwordchange.html', {'form': form})


class UpdateAccountView(View):
    def get(self, request):
        form = SignForm(instance=request.user)
        return render(request, 'upadte_account.html', {'form': form})


class EditworkView(View):
    def get(self, request, id):
        mywork = AddClassWork.objects.get(pk=id)
        form = AddClassWorkForm(instance=mywork)
        return render(request, 'editwork.html', {'form': form})

    def post(self, request, id):
        mywork = AddClassWork.objects.get(pk=id)
        form = AddClassWorkForm(request.POST, request.FILES, instance=mywork)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return render(request, 'editwork.html', {'form': form})


class ExamView(View):
    def get(self, request, id):

        form = QuesModelForm()
        mywork = CreateClass.objects.get(pk=id)
        exam = QuesModel.objects.filter(myclass=mywork)[::-1]
        return render(request, 'exam-info.html', {'mainid': id, 'form': form, 'exam': exam})

    def post(self, request, id):

        mywork = CreateClass.objects.get(pk=id)
        form = QuesModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.myclass = mywork
            obj.save()
            messages.success(request, "Successfully Saved")
        exam = QuesModel.objects.filter(myclass=mywork)[::-1]
        return render(request, 'exam-info.html', {'form': form, 'mainid': id,  'exam': exam})


class ShowQuizView(View):
    def get(self, request, id):
        allquiz = QuesModel.objects.filter(id=id)
        return render(request, 'allquiz.html', {'allquiz': allquiz})


class EditAnnouceView(View):
    def get(self, request, id):
        mywork = Announcement.objects.get(pk=id)
        form = AnnouncementForm(instance=mywork)
        return render(request, 'editlist.html', {'form': form})

    def post(self, request, id):
        mywork = Announcement.objects.get(pk=id)
        form = AnnouncementForm(request.POST, instance=mywork)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return render(request, 'editlist.html', {'form': form})


def pdf_view(request, id):

    maindata = AddClassWork.objects.get(pk=id)
    mainfile = maindata.document

    fs = FileSystemStorage()
    filename = str(mainfile)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # user will be prompted display the PDF in the browser
            response['Content-Disposition'] = 'inline; filename="filename"'

            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


class MyCourse(View):
    def get(self, request):
        courseview = ViewCourse.objects.filter(
            teachercourse=request.user)
        return render(request, "course.html", {'courseview': courseview})


class MyCourseform(View):
    def get(self, request):
        form = ViewCourseForm()
        return render(request, "addcourse.html", {'form': form})

    def post(self, request):
        form = ViewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.teachercourse = request.user
            obj.save()
            messages.success(request, "Successfulloy Added Course")
            return redirect('addlink')
        return render(request, "addcourse.html", {'form': form})


class MyLinkform(View):
    def get(self, request):
        form = AddlinkForm()
        return render(request, "addlink.html", {'form': form})

    def post(self, request):
        form = AddlinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfulloy Added Link")
            return redirect("mycourse")
        return render(request, "addlink.html", {'form': form})


class MyCourseView(View):
    def get(self, request, id):
        coursen = ViewCourse.objects.get(pk=id)
        courseview = AddCourse.objects.filter(course=coursen)
        return render(request, "viewcourse.html", {'courseview': courseview})


class ComentreplyView(View):
    def post(self, request, id):
        comment = CommentMain.objects.get(id=id)
        replytext = request.POST.get("replytext")
        replycom = ReplyComment(annoucemain=comment, text=replytext)
        replycom.save()
        messages.success(
            request, f"You Reply {comment.mystu.first_name} {comment.mystu.last_name} Comment")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleltecomment(request, id):
    comment = CommentMain.objects.get(id=id)
    comment.delete()
    messages.warning(request, "Delete Comment Succesfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def showreply(request, id):

    comment = CommentMain.objects.get(id=id)
    allreply = ReplyComment.objects.filter(annoucemain=comment)
    return render(request, 'annview.html', {"allreply": allreply})
