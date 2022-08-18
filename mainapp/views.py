from pyexpat.errors import messages
from re import M
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.views import View
from .forms import SignForm, StudentRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from .models import Student


class LoginTeacherView(View):
    def get(self, request):

        fm = LoginForm()
        return render(request, 'login_teacher.html', {'form': fm, 'teacher_login': 'active'})

    def post(self, request):
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/teacher')
            else:
                messages.warning(request, 'Email Or Password Invalid')
                return redirect("/")
        return render(request, 'login_teacher.html', {'form': fm, 'teacher_login': 'active'})


class LoginStudentView(View):
    return_url = None

    def get(self, request):
        LoginStudentView.return_url = request.GET.get('return_url')
        return render(request, 'login_student.html', {'student_login': 'active'})

    def post(self, request):
        student_id = request.POST.get('id_no')
        password = request.POST.get('password')

        student = Student.get_student_by_id(student_id)

        if student:
            flag = check_password(password, student.password)
            if flag:
                request.session['student'] = student.id
                return redirect('/student')
            else:
                messages.warning(request, "id Or Password Invalid")
        else:
            messages.warning(request, "id Or Password Invalid")

        return render(request, 'login_student.html', {'student_login': 'active'})


class RegisterTeacherView(View):
    def get(self, request):
        fm = SignForm()
        return render(request, 'register_teacher.html', {'form': fm, 'teacher_register': 'active'})

    def post(self, request):
        fm = SignForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Saved  successfully!')
            fm.save()
        return render(request, 'register_teacher.html', {'form': fm, 'teacher_register': 'active'})


class RegisterStudentView(View):
    def get(self, request):
        fm = StudentRegisterForm()
        return render(request, 'register_student.html', {'form': fm, 'student_register': 'active'})

    def post(self, request):
        fm = StudentRegisterForm(request.POST)
        if fm.is_valid():
            password = fm.cleaned_data['password']
            cpassword = fm.cleaned_data['cpassword']

            if password != cpassword:
                messages.warning(request, 'Password Not Match')
            mypassword = make_password(password)
            mypassword1 = make_password(cpassword)
            obj = fm.save(commit=False)
            obj.password = mypassword
            obj.cpassword = mypassword1
            obj.save()
            messages.success(request, 'Saved  successfully!')
        else:
            messages.warning(request, 'Not Saved')

        return render(request, 'register_student.html', {'form': fm, 'student_register': 'active'})
