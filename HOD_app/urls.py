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

    # Subjects
    path('Hod/Subject/Add', AddSubjectView.as_view(), name="add_subject"),
    path('Hod/Subject/View', ViewSubjectView.as_view(), name="view_subject"),
    path('Hod/Subject/Edit/<str:id>', EditSubjectView.as_view(), name="edit_subject"),
    path('Hod/Subject/Update', UpdateSubjectView.as_view(), name="update_subject"),
    path('Hod/Subject/Delete/<str:id>', DeleteSubjectView.as_view(), name="delete_subject"),

    # Session
    path('Hod/Session/Add', AddSessionView.as_view(), name="add_session"),
    path('Hod/Session/View', ViewSessionView.as_view(), name="view_session"),
    path('Hod/Session/Edit/<str:id>', EditSessionView.as_view(), name="edit_session"),
    path('Hod/Session/Update', UpdateSessionView.as_view(), name="update_session"),
    path('Hod/Session/Delete/<str:id>', DeleteSessionView.as_view(), name="delete_session"),

    # Staff Notifications
    path('Hod/Staff/Send_Notification', StaffSendNotification.as_view(), name="staff_send_notification"),
    path('Hod/Staff/Save_Notification', SaveStaffNotification.as_view(), name="save_staff_notification"),

    # Student Notification
    path('Hod/Student/Send_Notification', StudentSendNotification.as_view(), name="student_send_notification"),
    path('Hod/Student/Save_Notification', SaveStudentNotification.as_view(), name="save_student_notification"),

    # Staff Leave View
    path('Hod/Staff/Leave_view', StaffLeaveView.as_view(), name="staff_leave_view"),
    path('Hod/Staff/approve_leave/<str:id>', StaffApproveLeaveView.as_view(), name="staff_approve_leave"),
    path('Hod/Staff/disapprove_leave/<str:id>', StaffDisapproveLeaveView.as_view(), name="staff_disapprove_leave"),

    # Staff Feedback
    path('Hod/Staff/Feedback_reply', StaffFeedbackView.as_view(), name="staff_feedback_reply"),
    path('Hod/Staff/Feedback_reply_save', StaffFeedbackReplySaveView.as_view(), name="staff_feedback_reply_save"),

    # Student Feedback
    path('Hod/Student/Feedback_reply', StudentFeedbackView.as_view(), name="student_feedback_reply"),
    path('Hod/Student/Feedback_reply_save', StudentFeedbackReplySaveView.as_view(), name="student_feedback_reply_save"),

    # Student Leave View
    path('Hod/Student/Leave_view', StudentLeaveView.as_view(), name="student_leave_view"),
    path('Hod/Student/approve_leave/<str:id>', StudentApproveLeaveView.as_view(), name="student_approve_leave"),
    path('Hod/Student/disapprove_leave/<str:id>', StudentDisapproveLeaveView.as_view(), name="student_disapprove_leave"),

    # Attendance
    path('Hod/View/Attendance', views.ViewAttendance, name="view_attendance"),

]
