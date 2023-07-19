from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Student_app.models import Students
from .models import Staffs
from student_management_app.models import Courses, SessionYearModel, CustomUser, Students, Subjects
from django.contrib import messages
from student_management_app.models import NotificationStaffs, LeaveReportStaff, FeedBackStaffs, Attendance, AttendanceReport, StudentResult


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

# @method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
# class StaffTakeAttendanceView(View):
#     def get(self, request):
#         staff_id = Staffs.objects.filter(admin=request.user.id)
#
#         # for staffs in staff:
#         #     staff_id = staffs.id
#
#         subject = Subjects.objects.filter(staff_id=request.user.id)
#         session = SessionYearModel.objects.all()
#
#         subject_id = request.GET.get('subject_id', None)
#         # session_id = request.GET.get('session_id')
#         if subject_id is not None:
#             get_subject = Subjects.objects.get(id=subject_id)
#         else:
#             get_subject = None
#
#         # get_session_year = SessionYearModel.objects.get(id=session_id)
#
#
#         context = {
#             "subjects": subject,
#             "session": session,
#             "get_subject": get_subject,
#             # "get_session_year": get_session_year,
#             # "action": action,
#         }
#         return render(request, "Staff_template/take_attendance.html", context)



# class StaffTakeAttendanceView(View):
#     def get(self, request):
#         staff_id = Staffs.objects.get(admin=request.user.id)
#
#         subject = Subjects.objects.filter(staff_id=request.user.id)
#         session_year = SessionYearModel.objects.all()
#         action = request.GET.get('action')
#
#         get_subject = None
#         get_session_year = None
#         if action is not None:
#             subject_id = request.GET.get('subject_id')
#             session_id = request.GET.get('session_id')
#
#             get_subject = Subjects.objects.get(id=subject_id)
#             get_session_year = SessionYearModel.objects.get(id=session_id)
#
#
#         context = {
#             "subject": subject,
#             "session_year": session_year,
#             "get_subject": get_subject,
#             "get_session_year": get_session_year,
#             "action": action,
#         }
#         return render(request, "Staff_template/take_attendance.html", context)
#
#     def post(self, request):
#         staff = Staffs.objects.get(admin=request.user)
#         subjects = Subjects.objects.filter(staff_id=request.user)
#         session_years = SessionYearModel.objects.all()
#         action = request.POST.get('action')
#
#         get_subject = None
#         get_session_year = None
#         if action:
#             subject_id = request.POST.get('subject_id')
#             session_id = request.POST.get('session_id')
#
#             try:
#                 get_subject = Subjects.objects.get(id=subject_id)
#                 get_session_year = SessionYearModel.objects.get(id=session_id)
#
#                 # Process the form data from the request
#                 # ...
#
#                 # Optionally, you can redirect to a success page or perform any other necessary actions
#                 return redirect('success_page')
#             except (Subjects.DoesNotExist, SessionYearModel.DoesNotExist):
#                 # Handle the case when the subject or session year is not found
#                 messages.error(request, 'Invalid subject or session year')
#                 return redirect('error_page')
#
#         context = {
#             "subjects": subjects,
#             "session_years": session_years,
#             "get_subject": get_subject,
#             "get_session_year": get_session_year,
#             "action": action,
#         }
#         return render(request, "Staff_template/take_attendance.html", context)

def StaffTakeAttendance(request ):
    staff_id = Staffs.objects.get(admin=request.user.id)

    # subject = Subjects.objects.filter(staff=staff_id.id)
    subject = Subjects.objects.filter(staff=request.user.id)
    print(subject)
    session_year = SessionYearModel.objects.all()
    action = request.GET.get('action')

    students = None
    get_subject = None
    get_session_year = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subjects.objects.get(id=subject_id)
            get_session_year = SessionYearModel.objects.get(id=session_year_id)

            subject = Subjects.objects.filter(id=subject_id)
            for subjects in subject:
                student_id = subjects.course_id.id
                students = Students.objects.filter(course_id=student_id)

    context = {
        "subjects": subject,
        "session_year": session_year,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "action": action,
        "students": students,
    }
    return render(request, "Staff_template/take_attendance.html", context)


def StaffSaveAttendance(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')


        get_subject = Subjects.objects.get(id=subject_id)
        get_session_year = SessionYearModel.objects.get(id=session_year_id)

        attendance = Attendance(
            # subject_id=get_subject,
            # subject=subject_id,
            subject=get_subject,
            attendance_date=attendance_date,
            session_year=get_session_year,
        )
        attendance.save()
        for student_ids in student_id:
            stud_id = student_ids
            # stud_id = int(student_ids)
            int_stud = int(stud_id)

            p_students = Students.objects.get(id=int_stud)
            # p_students = Students.objects.get(id=stud_id)
            attendance_report = AttendanceReport(
                student=p_students,
                # student_id=p_students,
                attendance=attendance,
            )
            attendance_report.save()
            messages.success(request, "Attendance Taken Successfully")
    return redirect("Staff_app:staff_take_attendance")

# def StaffSaveAttendance(request):
#     if request.method == "POST":
#         subject = request.POST.get('subject')
#         session_year_id = request.POST.get('session_year_id')
#         attendance_date = request.POST.get('attendance_date')
#         student_id = request.POST.getlist('student_id')
#
#         get_subject = Subjects.objects.get(id=subject)
#         print(get_subject)
#         get_session_year = SessionYearModel.objects.get(id=session_year_id)
#
#         attendance = Attendance(
#             subject=get_subject,
#             attendance_date=attendance_date,
#             session_year_id=get_session_year,
#         )
#         attendance.save()
#         for student_ids in student_id:
#             stud_id = int(student_ids)
#             # int_stud = int(stud_id)
#
#             p_students = Students.objects.get(id=stud_id)
#             attendance_report = AttendanceReport(
#                 student_id=p_students,
#                 attendance_id=attendance,
#             )
#             attendance_report.save()
#             messages.success(request, "Attendance Taken Successfully")
#             return redirect("Staff_app:staff_take_attendance")



def StaffViewAttendance(request):
    staff_id = Staffs.objects.get(admin=request.user.id)

    subject = Subjects.objects.filter(staff=request.user.id)
    session_year = SessionYearModel.objects.all()

    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subjects.objects.get(id=subject_id)
            get_session_year = SessionYearModel.objects.get(id=session_year_id)
            attendance = Attendance.objects.filter(
                subject=get_subject,
                attendance_date=attendance_date,
            )
            for attendances in attendance:
                attendance = attendances.id
                attendance_report = AttendanceReport.objects.filter(
                    attendance_id=attendance,
                    student_id=request.user.id,
                )

    context = {
        "subjects": subject,
        "session_year": session_year,
        "action": action,
        "get_subject": get_subject,
        "get_session_year":  get_session_year,
        "attendance_date": attendance_date,
        "attendance_report":  attendance_report,
    }
    return render(request, "Staff_template/view_attendance.html", context)

class StaffAddResultView(View):
    def get(self, request):
        staff = Staffs.objects.get(admin=request.user.id)
        subjects = Subjects.objects.filter(staff_id=request.user.id)
        session_year = SessionYearModel.objects.all()
        action = request.GET.get('action')

        context = {
            "subjects": subjects,
            "session_year": session_year,
            "action": action,
        }
        return render(request, "Staff_template/add_result.html", context)

    def post(self, request):
        staff = Staffs.objects.get(admin=request.user.id)
        subjects = Subjects.objects.filter(staff_id=request.user.id)
        session_year = SessionYearModel.objects.all()
        action = request.GET.get('action')

        get_subject = None
        get_session = None
        students = None
        if action is not None:
            if request.method == "POST":
                subject_id = request.POST.get('subject_id')
                session_year_id = request.POST.get('session_year_id')

                get_subject = Subjects.objects.get(id=subject_id)
                get_session = SessionYearModel.objects.get(id=session_year_id)

                subjects = Subjects.objects.filter(id=subject_id)
                for subject in subjects:
                    student_id = subject.course_id.id
                    students = Students.objects.filter(course_id=student_id)

        context = {
            "subjects": subjects,
            "session_year": session_year,
            "action": action,
            "get_subject": get_subject,
            "get_session": get_session,
            "students": students,
        }
        return render(request, "Staff_template/add_result.html", context)

class StaffSaveResultView(View):
    def post(self, request):
        if request.method == "POST":
            student_id = request.POST.get('student_id')
            subject_id = request.POST.get('subject_id')
            session_year = request.POST.get('session_year')
            subject_assignment_marks = request.POST.get('subject_assignment_marks')
            subject_exam_marks = request.POST.get('subject_exam_marks')


            get_student = Students.objects.get(admin=student_id)
            get_subject = Subjects.objects.get(id=subject_id)

            check_exists = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
            if check_exists:
                result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
                result.subject_assignment_marks = subject_assignment_marks
                result.subject_exam_marks = subject_exam_marks
                result.save()
                messages.success(request, "Result Updated Successfully")
                return redirect("Staff_app:staff_add_result")
            else:
                result = StudentResult(
                    student=get_student,
                    subject=get_subject,
                    subject_assignment_marks=subject_assignment_marks,
                    subject_exam_marks=subject_exam_marks,
                )
                result.save()
                messages.success(request, "Result Added Successfully")
                return redirect("Staff_app:staff_add_result")

