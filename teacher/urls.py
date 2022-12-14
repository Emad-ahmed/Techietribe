from django.urls import path
from .views import MyCourseform, TeacherHome, CreateClassview, ClassShow, deleltecomment, userlogout, deletecard, deletelist, Addworkview, ShowWorkview, deletework, PasswordChangeView, UpdateAccountView, pdf_view, EditworkView, EditAnnouceView, ExamView, ShowQuizView, MyCourse, MyCourseform, MyLinkform, MyCourseView, AnnView, ComentreplyView, showreply, JoinClassViewTeach, FullClassworkView, AnnouceViewTeach, EditCommentviewTeach, WorkViewteacher, FullWorkViewTeach, PeopleView, ExamShowTeacher, deletejoinclassteach, show_people_work_view
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
    path('annonceshow/<int:id>/', AnnView.as_view(), name='annonceshow'),
    path('comentreply/<int:id>/', ComentreplyView.as_view(), name='comentreply'),
    path('deleltecomment/<int:id>/', deleltecomment, name='deleltecomment'),
    path('showreply/<int:id>/', showreply, name='showreply'),
    path('joinclassteach', JoinClassViewTeach.as_view(), name='joinclassteach'),
    path('class_view_work_teach/<int:id>/',
         FullClassworkView.as_view(), name='class_view_work_teach'),
    path('annouceviewteach/<int:id>/',
         AnnouceViewTeach.as_view(), name='annouceviewteach'),
    path('editcomteach/<int:id>/',
         EditCommentviewTeach.as_view(), name='editcomteach'),
    path('classworkviewteach/<int:id>/',
         WorkViewteacher.as_view(), name='classworkviewteach'),
    path('fullworkviewteach/<int:id>/',
         FullWorkViewTeach.as_view(), name='fullworkviewteach'),
    path('peopleview/<int:id>/',
         PeopleView.as_view(), name='peopleview'),
    path('examshowteach/<int:id>/',
         ExamShowTeacher.as_view(), name='examshowteach'),
    path('deletejoinclassteach/<int:id>/',
         deletejoinclassteach, name='deletejoinclassteach'),
    path('show_people_work_view/<int:id>/',
         show_people_work_view, name='show_people_work_view'),
]
