from django.urls import path
from .views import MyCourseform, TeacherHome, CreateClassview, ClassShow, userlogout, deletecard, deletelist, Addworkview, ShowWorkview, deletework, PasswordChangeView, UpdateAccountView, pdf_view, EditworkView, EditAnnouceView, ExamView, ShowQuizView, MyCourse, MyCourseform, MyLinkform, MyCourseView
urlpatterns = [
    path('', TeacherHome.as_view(), name='home'),
    path('create', CreateClassview.as_view(), name='create'),
    path('classshow/<int:id>/', ClassShow.as_view(), name='classshow'),
    path('addwork/<int:id>/', Addworkview.as_view(), name='addwork'),
    path('showmywork/<int:id>/', ShowWorkview.as_view(), name='showmywork'),
    path('editwork/<int:id>/', EditworkView.as_view(), name='editwork'),
    path('editlist/<int:id>/', EditAnnouceView.as_view(), name='editlist'),
    path('change_password', PasswordChangeView.as_view(), name='change_password'),
    path('update_account', UpdateAccountView.as_view(), name='update_account'),
    path('examview/<int:id>/', ExamView.as_view(), name='examview'),
    path('showquiz/<int:id>/', ShowQuizView.as_view(), name='showquiz'),
    path('userlogout', userlogout, name='userlogout'),
    path('deletecard/<int:id>/', deletecard, name='deletecard'),
    path('deletelist/<int:id>/', deletelist, name='deletelist'),
    path('deletework/<int:id>/', deletework, name='deletework'),
    path('pdf_view/<int:id>', pdf_view, name='pdf_view'),
    path('mycourse', MyCourse.as_view(), name='mycourse'),
    path('mycourseform', MyCourseform.as_view(), name='mycourseform'),
    path('addlink', MyLinkform.as_view(), name='addlink'),
    path('view_course/<int:id>/', MyCourseView.as_view(), name='view_course'),

]
