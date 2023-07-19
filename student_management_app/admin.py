from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SessionYearModel, CustomUser, Courses, Subjects, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs, StudentResult


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']


admin.site.register(SessionYearModel)
admin.site.register(CustomUser, UserModel)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
admin.site.register(StudentResult)