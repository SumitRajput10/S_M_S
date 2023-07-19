from django.urls import path
from .views import *
from . import views

app_name = 'Student_app'



urlpatterns = [
    path('Student/Home', StudentHomeView.as_view(), name="student_home"),


    # Notifications
    path('Student/Notifications', StudentNotificationsView.as_view(), name="notifications"),
    path('Student/mark_as_done/<str:status>', StudentMarkAsDoneView.as_view(), name="student_mark_as_done"),

    # Feedback
    path('Student/Feedback', StudentFeedbackView.as_view(), name="student_feedback"),
    path('Student/Feedback_save', StudentFeedbackSaveView.as_view(), name="student_feedback_save"),

    # Apply Leave
    path('Student/Apply_Leave', StudentApplyLeaveView.as_view(), name="student_apply_leave"),
    path('Student/Apply_Leave_save', StudentApplyLeaveSaveView.as_view(), name="student_apply_leave_save"),

    # Attendance
    path("Student/Attendance", views.StudentViewAttendance, name="student_view_attendance"),

    # Result
    path("Student/view_Result", views.ViewResult, name="view_result"),


]