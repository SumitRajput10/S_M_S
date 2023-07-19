from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Students
# from Staffs.models import Staffs
from student_management_app.models import Courses, SessionYearModel, CustomUser, Students, Subjects
from django.contrib import messages
from student_management_app.models import NotificationStaffs, LeaveReportStaff, FeedBackStaffs, NotificationStudent, FeedBackStudent, LeaveReportStudent, Attendance, AttendanceReport, StudentResult




@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentHomeView(View):
    def get(self, request):
        return render(request, "Student_template/home.html")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentNotificationsView(View):
    def get(self, request):
        student = Students.objects.filter(admin=request.user.id)
        for students in student:
            student_id = students.id
            notification = NotificationStudent.objects.filter(student_id=student_id)

            context = {
                "notification": notification
            }
            return render(request, "Student_template/notification.html", context)


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentMarkAsDoneView(View):
    def get(self, request, status):
        notification = NotificationStudent.objects.get(id=status)
        notification.status = 1
        notification.save()
        return redirect("Student_app:notifications")


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentFeedbackView(View):
    def get(self, request):
        student = Students.objects.filter(admin=request.user.id)
        for students in student:
            student_id = students.id
            feedback_history = FeedBackStudent.objects.filter(student_id=student_id)

            context = {
                "feedback_history": feedback_history
            }
            return render(request, "Student_template/feedback.html", context)
        return render(request, "Student_template/feedback.html")


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentFeedbackSaveView(View):
    def post(self, request):
        feedback = request.POST.get('feedback')
        student = Students.objects.filter(admin=request.user.id)
        for students in student:
            student_id = students.id
            feedback_history = FeedBackStudent(
                student_id=student_id,
                feedback=feedback,
                feedback_reply=" "
            )
            feedback_history.save()
            messages.success(request, "Feedback Submitted Successfully")
            return redirect("Student_app:student_feedback")


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentApplyLeaveView(View):
    def get(self, request):
        student = Students.objects.filter(admin=request.user.id)
        for students in student:
            student_id = students.id

            student_leave_history = LeaveReportStudent.objects.filter(student_id=student_id)

            context = {
                "student_leave_history": student_leave_history
            }
            return render(request, "Student_template/apply_leave.html", context)
        return render(request, "Student_template/apply_leave.html")


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentApplyLeaveSaveView(View):
    def post(self, request):
        leave_date = request.POST.get("leave_date")
        leave_message = request.POST.get("leave_message")

        student = Students.objects.get(admin=request.user.id)
        leave = LeaveReportStudent(
            student=student,
            leave_date=leave_date,
            leave_message=leave_message,
        )

        leave.save()
        messages.success(request, "Applied for leave Successfully")
        return redirect("Student_app:student_apply_leave")


def StudentViewAttendance(request):
    student = Students.objects.get(admin=request.user.id)
    subject = Subjects.objects.filter(course_id=student.course_id)
    action = request.GET.get('action')

    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            get_subject = Subjects.objects.get(id=subject_id)

            # attendance = Attendance.objects.get(subject_id=subject_id)
            attendance_report = AttendanceReport.objects.filter(student=student, attendance__subject=subject_id)
    context = {
        "subject": subject,
        "action": action,
        "get_subject": get_subject,
        "attendance_report": attendance_report,
    }

    return render(request, "Student_template/view_attendance.html", context)

#
# def ViewResult(request):
#     total_marks = ()
#     student = Students.objects.get(admin=request.user.id)
#     result = StudentResult.objects.filter(student_id=student.id)
#     print(result)
#
#     total_marks1=[]
#     for results in result:
#         subject_assignment_marks = results.subject_assignment_marks
#         subject_exam_marks = results.subject_exam_marks
#         total_marks = subject_assignment_marks + subject_exam_marks
#         total_marks1.append(total_marks)
#     print(total_marks)
#
#     context = {
#         "result": result,
#         "total_marks": total_marks,
#     }
#
#     return render(request, "Student_template/view_result.html", context)

def ViewResult(request):
    student = Students.objects.get(admin=request.user.id)
    results = StudentResult.objects.filter(student_id=student.id)

    context = {
        "results": results,
    }

    return render(request, "Student_template/view_result.html", context)
