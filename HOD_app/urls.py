from django.urls import path
from .views import *
from . import views

app_name = 'HOD_app'


urlpatterns = [
    path('Hod/Home', AdminHomeView.as_view(), name="hod_home"),
    path('Hod/Student/Add', AddStudentView.as_view(), name="add_student"),
    # path('add_student/', views.Add_Student, name='add_student'),
    path('Hod/Student/View', ViewStudentView.as_view(), name="view_student"),
    path('Hod/Student/Edit/<str:id>', EditStudentView.as_view(), name="edit_student"),
    path('Hod/Student/Update', UpdateStudentView.as_view(), name="update_student"),
    path('Hod/Student/Delete/<str:admin>', DeleteStudentView.as_view(), name="delete_student"),

    # Course
    path('Hod/Course/Add', AddCourseView.as_view(), name="add_course"),
    path('Hod/Course/View', ViewCourseView.as_view(), name="view_course"),
    path('Hod/Course/Edit/<str:id>', EditCourseView.as_view(), name="edit_course"),
    path('Hod/Course/Update', UpdateCourseView.as_view(), name="update_course"),
    path('Hod/Course/Delete/<str:id>', DeleteCourseView.as_view(), name="delete_course"),

    # Staff
    path('Hod/Staff/Add', AddStaffView.as_view(), name="add_staff"),
    path('Hod/Staff/View', ViewStaffView.as_view(), name="view_staff"),
    path('Hod/Staff/Edit/<str:id>', EditStaffView.as_view(), name="edit_staff"),
    path('Hod/Staff/Update', UpdateStaffView.as_view(), name="update_staff"),
    path('Hod/Staff/Delete/<str:admin>', DeleteStaffView.as_view(), name="delete_staff"),
]
