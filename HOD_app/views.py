from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Student_app.models import Students
from Staff_app.models import Staffs
from student_management_app.models import Courses, SessionYearModel, CustomUser, Students, Subjects
from django.contrib import messages
# from student_management_app.models import Subjects, Courses, Attendance, LeaveReportStaff, LeaveReportStudent, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, SessionYearModel, Attendance, AttendanceReport, CustomUser
from student_management_app.models import NotificationStaffs, LeaveReportStaff, FeedBackStaffs, NotificationStudent, LeaveReportStudent, FeedBackStudent, Attendance, AttendanceReport


# For downloading
import xlwt
from django.http import HttpResponse





# Create your views here.
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AdminHomeView(View):
    def get(self, request):
        student_count = Students.objects.all().count()
        staff_count = Staffs.objects.all().count()
        course_count = Courses.objects.all().count()
        subject_count = Subjects.objects.all().count()

        student_gender_male = Students.objects.filter(gender='Male').count()
        student_gender_female = Students.objects.filter(gender='Female').count()

        context = {
            'student_count': student_count,
            'staff_count': staff_count,
            'course_count': course_count,
            'subject_count': subject_count,
            'student_gender_male': student_gender_male,
            'student_gender_female': student_gender_female,
        }
        # print(context)
        return render(request, "HOD_template/home.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AddStudentView(View):
    def get(self, request):
        course = Courses.objects.all()
        session_year = SessionYearModel.objects.all()
        context = {
            'course': course,
            'session_year': session_year,
        }
        return render(request, "HOD_template/add_student.html", context)

    def post(self, request):
        course = Courses.objects.all()
        session_year = SessionYearModel.objects.all()

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        # print(profile_pic, first_name, last_name, email, username, password, address, gender, course_id, session_year_id)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('HOD_app:add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('HOD_app:add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,
            )
            user.set_password(password)
            user.save()

            course = Courses.objects.get(id=course_id)
            # student.course_id = course

            session_year = SessionYearModel.objects.get(id=session_year_id)
            # student.session_year_id = session_year

            student = Students(
                admin=CustomUser.objects.get(id=user.id),
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            # print("Before Save")
            student.save()
            # print("After Save")
            messages.success(request, user.first_name + " " + user.last_name + " are successfully added!")
            # messages.success(request, "Student Added Successfully!")
            return redirect('HOD_app:add_student')

        context = {
            'course': course,
            'session_year': session_year,

        }

        return render(request, "HOD_template/add_student.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ViewStudentView(View):
    def get(self, request):
        student = Students.objects.all()

        context = {
            'student': student,
        }

        return render(request, "HOD_template/view_student.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditStudentView(View):
    def get(self, request, id):
        student = Students.objects.filter(id=id)
        course = Courses.objects.all()
        session_year = SessionYearModel.objects.all()

        context = {
            'student': student,
            'course': course,
            'session_year': session_year,
        }

        return render(request, "HOD_template/edit_student.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class UpdateStudentView(View):
    def get(self, request):
        return render(request, "HOD_template/edit_student.html")

    def post(self, request):
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Students.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Courses.objects.get(id=course_id)
        student.course_id = course
        session_year = SessionYearModel.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, "Record Updated Successfully!")
        return redirect('HOD_app:view_student')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class DeleteStudentView(View):
    def get(self, request, admin):
        student = CustomUser.objects.get(id=admin)
        student.delete()
        messages.success(request, "Record Deleted Successfully!")
        return redirect('HOD_app:view_student')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AddCourseView(View):
    def get(self, request):
        return render(request, "HOD_template/add_course.html")

    def post(self, request):
        course_name = request.POST.get('course_name')

        course = Courses(
            course_name=course_name,
        )
        course.save()
        messages.success(request, "Course Added Successfully")
        return render(request, "HOD_template/add_course.html")

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ViewCourseView(View):
    def get(self, request):
        course = Courses.objects.all()
        context = {
            'course': course,
        }

        return render(request, "HOD_template/view_course.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditCourseView(View):
    def get(self, request, id):
        course = Courses.objects.filter(id=id)
        context = {
            'course': course,
        }

        return render(request, "HOD_template/edit_course.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class UpdateCourseView(View):
    def get(self, request):
        return render(request, "HOD_template/edit_course.html")

    def post(self, request):
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')

        # print(course_name, course_id)
        course = Courses.objects.get(id=course_id)
        course.course_name = course_name
        course.save()
        messages.success(request, "Courses Updated Successfully!")

        return redirect('HOD_app:view_course')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class DeleteCourseView(View):
    def get(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        messages.success(request, "Course Deleted Successfully!")
        return redirect('HOD_app:view_course')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AddStaffView(View):
    def get(self, request):
        return render(request, "HOD_template/add_staff.html")

    def post(self, request):
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        print(profile_pic, first_name, last_name,email,username,password,address,phone_number,gender)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('HOD_app:add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('HOD_app:add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            staff = Staffs(
                admin=user,
                address=address,
                phone_number=phone_number,
                gender=gender,
            )
            staff.save()
            messages.success(request, user.first_name + " " + user.last_name + " are successfully added!")
            return redirect('HOD_app:add_staff')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ViewStaffView(View):
    def get(self, request):
        staff = Staffs.objects.all()
        context = {
            'staff': staff,
        }

        return render(request, "HOD_template/view_staff.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditStaffView(View):
    def get(self, request, id):
        staff = Staffs.objects.filter(id=id)
        context = {
            'staff': staff,
        }

        return render(request, "HOD_template/edit_staff.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class UpdateStaffView(View):
    def get(self, request):
        return render(request, "HOD_template/edit_staff.html")

    def post(self, request):
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staffs.objects.get(admin=staff_id)
        staff.address = address
        staff.phone_number = phone_number
        staff.gender = gender

        staff.save()
        messages.success(request, "Record Updated Successfully!")
        return redirect('HOD_app:view_staff')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class DeleteStaffView(View):
    def get(self, request, admin):
        staff = CustomUser.objects.get(id=admin)
        staff.delete()
        messages.success(request, "Record Deleted Successfully!")
        return redirect('HOD_app:view_staff')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AddSubjectView(View):
    def get(self, request):
        course = Courses.objects.all()
        staff = Staffs.objects.all()
        context = {
            'course': course,
            'staff': staff,
        }
        return render(request, "HOD_template/add_subject.html", context)

    def post(self, request):

        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get('staff_id')
        staff = CustomUser.objects.get(id=staff_id)


        print(subject_name, course_id, staff_id)

        subject = Subjects(
            subject_name=subject_name,
            course_id=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subject Added Successfully!")
        return redirect('HOD_app:add_subject')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ViewSubjectView(View):
    def get(self, request):
        subject = Subjects.objects.all()
        context = {
            'subject': subject,
        }

        return render(request, "HOD_template/view_subject.html", context)
    
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditSubjectView(View):
    def get(self, request, id):
        subject = Subjects.objects.filter(id=id)
        course = Courses.objects.all()
        staff = Staffs.objects.all()
        context = {
            'subject': subject,
            'course': course,
            'staff': staff,
        }

        return render(request, "HOD_template/edit_subject.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class UpdateSubjectView(View):
    def get(self, request):
        return render(request, "HOD_template/edit_subject.html")

    def post(self, request):
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')


        subject = Subjects.objects.get(id=subject_id)
        subject.subject_name = subject_name
        course = Courses.objects.get(id=course_id)
        course.course_id = course_id
        subject.staff_id = staff_id
        # print(subject_id, subject_name, course_id, staff_id)
        subject.save()
        messages.success(request, "Record Updated Successfully!")
        return redirect('HOD_app:view_subject')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class DeleteSubjectView(View):
    def get(self, request, id):
        subject = Subjects.objects.get(id=id)
        subject.delete()
        messages.success(request, "Record Deleted Successfully!")
        return redirect('HOD_app:view_subject')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AddSessionView(View):
    def get(self, request):
        return render(request, "HOD_template/add_session.html")

    def post(self, request):
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        session = SessionYearModel(
            session_start_year=session_start_year,
            session_end_year=session_end_year,
        )
        session.save()
        messages.success(request, "Session Added Successfully!")
        return redirect('HOD_app:add_session')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ViewSessionView(View):
    def get(self, request):
        session = SessionYearModel.objects.all()
        context = {
            'session': session,
        }

        return render(request, "HOD_template/view_session.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditSessionView(View):
    def get(self, request, id):
        session = SessionYearModel.objects.filter(id=id)
        context = {
            'session': session,
        }

        return render(request, "HOD_template/edit_session.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class UpdateSessionView(View):
    def get(self, request):
        return render(request, "HOD_template/edit_session.html")

    def post(self, request):
        session_id = request.POST.get('session_id')
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        session = SessionYearModel.objects.get(id=session_id)
        session.session_start_year = session_start_year
        session.session_end_year = session_end_year
        session.save()
        messages.success(request, "Sessions Are Updated Successfully!")
        return redirect('HOD_app:view_session')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class DeleteSessionView(View):
    def get(self, request, id):
        session = SessionYearModel.objects.get(id=id)
        session.delete()
        messages.success(request, "Sessions Are Deleted Successfully!")
        return redirect('HOD_app:view_session')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffSendNotification(View):
    def get(self, request):
        staff = Staffs.objects.all()
        see_notification = NotificationStaffs.objects.all().order_by('-id')[0:5]

        context = {
            'staff': staff,
            'see_notification': see_notification,
        }
        return render(request, "HOD_template/staff_notification.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class SaveStaffNotification(View):
    def post(self, request):
        staff = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staffs.objects.get(id=staff).id
        notification = NotificationStaffs(staff_id=staff, message=message)
        notification.save()
        messages.success(request, "Notification Sent Successfully!")
        return redirect('HOD_app:staff_send_notification')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffLeaveView(View):
    def get(self, request):
        staff_leave = LeaveReportStaff.objects.all()
        context = {
            'staff_leave': staff_leave,
        }
        return render(request, "HOD_template/staff_leave.html", context)
    
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffApproveLeaveView(View):
    def get(self, request, id):
        leave = LeaveReportStaff.objects.get(id=id)
        leave.leave_status = 1
        leave.save()
        return redirect('HOD_app:staff_leave_view')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffDisapproveLeaveView(View):
    def get(self, request, id):
        leave = LeaveReportStaff.objects.get(id=id)
        leave.leave_status = 2
        leave.save()
        return redirect('HOD_app:staff_leave_view')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffFeedbackView(View):
    def get(self, request):
        feedback = FeedBackStaffs.objects.all()
        feedback_history = FeedBackStaffs.objects.all().order_by('-id')[0:5]

        context = {
            'feedback': feedback,
            'feedback_history': feedback_history
        }
        return render(request, "HOD_template/staff_feedback.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StaffFeedbackReplySaveView(View):
    def post(self, request):
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('HOD_app:staff_feedback_reply')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentSendNotification(View):
    def get(self, request):
        student = Students.objects.all()
        see_notification = NotificationStudent.objects.all().order_by('-id')[0:5]

        context = {
            'student': student,
            'see_notification': see_notification,
        }
        return render(request, "HOD_template/student_notification.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class SaveStudentNotification(View):
    def post(self, request):
        student = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Students.objects.get(id=student).id
        notification = NotificationStudent(student_id=student, message=message)
        notification.save()
        messages.success(request, "Notification Sent Successfully!")
        return redirect('HOD_app:student_send_notification')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentFeedbackView(View):
    def get(self, request):
        feedback = FeedBackStudent.objects.all()
        feedback_history = FeedBackStudent.objects.all().order_by('-id')[0:5]
        context = {
            'feedback': feedback,
            'feedback_history': feedback_history,
        }
        return render(request, "HOD_template/student_feedback.html", context)

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentFeedbackReplySaveView(View):
    def post(self, request):
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('HOD_app:student_feedback_reply')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentLeaveView(View):
    def get(self, request):
        student_leave = LeaveReportStudent.objects.all()
        context = {
            'student_leave': student_leave,
        }
        return render(request, "HOD_template/student_leave.html", context)


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentApproveLeaveView(View):
    def get(self, request, id):
        leave = LeaveReportStudent.objects.get(id=id)
        leave.leave_status = 1
        leave.save()
        return redirect('HOD_app:student_leave_view')

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class StudentDisapproveLeaveView(View):
    def get(self, request, id):
        leave = LeaveReportStudent.objects.get(id=id)
        leave.leave_status = 2
        leave.save()
        return redirect('HOD_app:student_leave_view')


def ViewAttendance(request):
    subject = Subjects.objects.all()
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
                )

    context = {
        "subjects": subject,
        "session_year": session_year,
        "action": action,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "attendance_date": attendance_date,
        "attendance_report": attendance_report,
    }
    return render(request, "HOD_template/view_attendance.html", context)











# For Download Excel Sheet
# def download_excel_data(request):
#     # dummy data
#     def get_data():
#         data = [
#             ['Column 1', 'Column 2', 'Column 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#             ['Value 1', 'Value 2', 'Value 3'],
#         ]
#         return data
#
#     # create a HttpResponse object and write the required excel data into it.
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('sheet1')
#     # Sheet header, first row
#     row_num = 0
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#     columns = ['Column 1', 'Column 2', 'Column 3']
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#         # Sheet body, remaining rows
#         font_style = xlwt.XFStyle()
#         rows = get_data()
#         for row_num in range(1, len(rows)):
#             for col_num in range(len(rows[row_num])):
#                 ws.write(row_num, col_num, rows[row_num][col_num], font_style)
#                 # save the file
#                 wb.save(response)
#                 return response
#                 # return response
#                 # return HttpResponse(response)
#                 # return response









