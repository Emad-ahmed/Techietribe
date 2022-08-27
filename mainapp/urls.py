from django.urls import path
from .views import LoginTeacherView, LoginStudentView, RegisterTeacherView, RegisterStudentView
from django.contrib.auth import views as auth_views
from mainapp.forms import MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('', LoginTeacherView.as_view(), name='home'),
    path('student_login', LoginStudentView.as_view(), name='student_login'),
    path('student_register', RegisterStudentView.as_view(), name='student_register'),
    path('teacher_register', RegisterTeacherView.as_view(), name='teacher_register'),


    # Password Reset


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
]
