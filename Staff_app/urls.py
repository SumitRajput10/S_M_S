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



]