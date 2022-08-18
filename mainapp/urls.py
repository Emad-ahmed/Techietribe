from django.urls import path
from .views import LoginTeacherView, LoginStudentView, RegisterTeacherView, RegisterStudentView

urlpatterns = [
    path('', LoginTeacherView.as_view(), name='home'),
    path('student_login', LoginStudentView.as_view(), name='student_login'),
    path('student_register', RegisterStudentView.as_view(), name='student_register'),
    path('teacher_register', RegisterTeacherView.as_view(), name='teacher_register'),
]
