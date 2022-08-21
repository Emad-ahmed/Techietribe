from django.urls import path
from .views import StudentHome, JoinClassView, ClassworkView, deleletwork, studentlogout, AnnouceView, WorkView, FullWorkView, deleletwork, FullCourseiew, FullCourseiewfull, deleltecommentstu, EditCommentview, showreplystu, EditStudent
urlpatterns = [
    path('', StudentHome.as_view(), name='home'),
    path('join_class', JoinClassView.as_view(), name='join_class'),
    path('class_view_work/<int:id>/',
         ClassworkView.as_view(), name='class_view_work'),
    path('full_course', FullCourseiew.as_view(), name='full_course'),
    path('studentlogout', studentlogout, name='studentlogout'),
    path('annouceview/<int:id>/', AnnouceView.as_view(), name='annouceview'),
    path('classworkview/<int:id>/', WorkView.as_view(), name='classworkview'),
    path('addclassworkfullview/<int:id>/',
         FullWorkView.as_view(), name='addclassworkfullview'),
    path('details_course_view/<int:id>/',
         FullCourseiewfull.as_view(), name='details_course_view'),

    path('deleletwork/<int:id>/',
         deleletwork, name='deleletwork'),
    path('deleltecommentstu/<int:id>/',
         deleltecommentstu, name='deleltecommentstu'),
    path('editcomment/<int:id>/',
         EditCommentview.as_view(), name='editcomment'),
    path('showreplystu/<int:id>/',
         showreplystu, name='showreplystu'),

    path('update_account_stu',
         EditStudent.as_view(), name='update_account_stu'),
]
