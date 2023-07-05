from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Student_app.models import Students
from .models import Staffs
from student_management_app.models import Courses, SessionYearModel, CustomUser, Students, Subjects
from django.contrib import messages
from student_management_app.models import NotificationStaffs, LeaveReportStaff, FeedBackStaffs


# from student_management_app.models import Subjects, Courses, Attendance, LeaveReportStaff, LeaveReportStudent, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, SessionYearModel, Attendance, AttendanceReport, CustomUser





@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffHomeView(View):
    def get(self, request):
        return render(request, "Staff_template/home.html")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffNotificationsView(View):
    def get(self, request):
        staff = Staffs.objects.filter(admin=request.user.id)
        for staffs in staff:
            staff_id = staffs.id
            notification = NotificationStaffs.objects.filter(staff_id=staff_id)

            context = {
                "notification": notification
            }
            return render(request, "Staff_template/notification.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffMarkAsDoneView(View):
    def get(self, request, status):
        notification = NotificationStaffs.objects.get(id=status)
        notification.status = 1
        notification.save()
        return redirect("Staff_app:notifications")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffApplyLeaveView(View):
    def get(self, request):
        staff = Staffs.objects.filter(admin=request.user.id)
        for staffs in staff:
            staff_id = staffs.id

            staff_leave_history = LeaveReportStaff.objects.filter(staff_id=staff_id)

            context = {
                "staff_leave_history": staff_leave_history
            }
            return render(request, "Staff_template/apply_leave.html", context)
        return render(request, "Staff_template/apply_leave.html")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffApplyLeaveSaveView(View):
    def post(self, request):
        leave_date = request.POST.get("leave_date")
        leave_message = request.POST.get("leave_message")

        staff = Staffs.objects.get(admin=request.user.id)
        leave = LeaveReportStaff(
            staff=staff,
            leave_date=leave_date,
            leave_message=leave_message,
        )

        leave.save()
        messages.success(request, "Applied for leave Successfully")
        return redirect("Staff_app:staff_apply_leave")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffFeedbackView(View):
    def get(self, request):
        staff = Staffs.objects.filter(admin=request.user.id)
        for staffs in staff:
            staff_id = staffs.id
            feedback_history = FeedBackStaffs.objects.filter(staff_id=staff_id)

            context = {
                "feedback_history": feedback_history
            }
            return render(request, "Staff_template/feedback.html", context)
        return render(request, "Staff_template/feedback.html")


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffFeedbackSaveView(View):
    def post(self, request):
        feedback = request.POST.get("feedback")
        staff = Staffs.objects.get(admin=request.user.id)
        feedback = FeedBackStaffs(
            staff=staff,
            feedback=feedback,
            feedback_reply=" ",
        )
        feedback.save()
        messages.success(request, "Feedback Submitted Successfully")
        return redirect("Staff_app:staff_feedback")