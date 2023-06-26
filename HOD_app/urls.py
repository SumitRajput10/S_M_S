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

]
