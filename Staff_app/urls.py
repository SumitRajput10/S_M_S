from django.urls import path
from .views import *
from . import views

app_name = 'Staff_app'



urlpatterns = [
    path('Staff/Home', StaffHomeView.as_view(), name="staff_home"),



    # Notifications
    path('Staff/Notifications', StaffNotificationsView.as_view(), name="notifications"),
    path('Staff/mark_as_done/<str:status>', StaffMarkAsDoneView.as_view(), name="staff_mark_as_done"),

    # Apply Leave
    path('Staff/Apply_Leave', StaffApplyLeaveView.as_view(), name="staff_apply_leave"),
    path('Staff/Apply_Leave_save', StaffApplyLeaveSaveView.as_view(), name="staff_apply_leave_save"),

    # Feedback
    path('Staff/Feedback', StaffFeedbackView.as_view(), name="staff_feedback"),
    path('Staff/Feedback_save', StaffFeedbackSaveView.as_view(), name="staff_feedback_save"),

    # Attendance
    # path('Staff/Take_Attendance', StaffTakeAttendanceView.as_view(), name="staff_take_attendance"),
    # path('Staff/Attendance_save', StaffAttendanceSaveView.as_view(), name="staff_attendance_save"),
    # path('Staff/Attendance_update', StaffAttendanceUpdateView.as_view(), name="staff_attendance_update"),
    # path('Staff/Attendance_delete', StaffAttendanceDeleteView.as_view(), name="staff_attendance_delete"),
    path('Staff/Take_Attendance', views.StaffTakeAttendance, name='staff_take_attendance'),
    path('Staff/Save_Attendance', views.StaffSaveAttendance, name='staff_save_attendance'),
    path('Staff/View_Attendance', views.StaffViewAttendance, name='staff_view_attendance'),

    # Result
    path('Staff/Add/Result', StaffAddResultView.as_view(), name="staff_add_result"),
    path('Staff/Save/Result', StaffSaveResultView.as_view(), name="staff_save_result"),

]