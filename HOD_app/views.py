from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Student_app.models import Students
from student_management_app.models import Courses, SessionYearModel, CustomUser, Students
from django.contrib import messages
# from student_management_app.models import Subjects, Courses, Attendance, LeaveReportStaff, LeaveReportStudent, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, SessionYearModel, Attendance, AttendanceReport, CustomUser








# Create your views here.
# @method_decorator(login_required, name='dispatch')
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class AdminHomeView(View):
    def get(self, request):
        return render(request, "HOD_template/home.html")



# @login_required(login_url='login')
# def Add_Student(request):
#     course = Courses.objects.all()
#     session_year = SessionYearModel.objects.all()
#
#     if request.method == "POST":
#         profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         address = request.POST.get('address')
#         gender = request.POST.get('gender')
#         course_id = request.POST.get('course_id')
#         session_year_id = request.POST.get('session_year_id')
#
#         print(profile_pic, first_name, last_name, email, username, password, address, gender, course_id, session_year_id)
#
#         if CustomUser.objects.filter(email=email).exists():
#             messages.warning(request, 'Email Is Already Taken')
#             return redirect('HOD_app:add_student')
#         if CustomUser.objects.filter(username=username).exists():
#             messages.warning(request, 'Username Is Already Taken')
#             return redirect('HOD_app:add_student')
#         else:
#             user = CustomUser(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 email=email,
#                 profile_pic=profile_pic,
#                 user_type=3,
#             )
#             user.set_password(password)
#             user.save()
#
#             course = Courses.objects.get(id=course_id)
#             # student.course_id = course
#             session_year = SessionYearModel.objects.get(id=session_year_id)
#             # student.session_year_id = session_year
#
#             student = Students(
#                 admin=user,
#                 address=address,
#                 session_year_id=session_year,
#                 course_id=course,
#                 gender=gender,
#             )
#
#             student.save()
#             messages.success(request, "Student Added Successfully!")
#             return redirect('HOD_app:add_student')
#
#     context = {
#         'course': course,
#         'session_year': session_year,
#     }
#
#
#     return render(request, "HOD_template/add_student.html", context)


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
        print(profile_pic, first_name, last_name, email, username, password, address, gender, course_id, session_year_id)

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
            print("Before Save")
            student.save()
            print("After Save")
            messages.success(request, user.first_name + " " + user.last_name + " are successfully added!")
            # messages.success(request, "Student Added Successfully!")
            return redirect('HOD_app:add_student')

        context = {
            'course': course,
            'session_year': session_year,

        }

        return render(request, "HOD_template/add_student.html", context)





# class AddStudentView(View):
#     def get(self, request):
#         course = Courses.objects.all()
#         session_year = SessionYearModel.objects.all()
#
#         if request.method == "POST":
#             profile_pic = request.FILES.get('profile_pic')
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             email = request.POST.get('email')
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             address = request.POST.get('address')
#             gender = request.POST.get('gender')
#             course_id = request.POST.get('course_id')
#             session_year_id = request.POST.get('session_year_id')
#             print(profile_pic, first_name, last_name, email, username, password, address, gender, course_id, session_year_id)
#
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.warning(request, 'Email Is Already Taken')
#                 return redirect('HOD_app:add_student')
#             if CustomUser.objects.filter(username=username).exists():
#                 messages.warning(request, 'Username Is Already Taken')
#                 return redirect('HOD_app:add_student')
#             else:
#                 user = CustomUser(
#                     first_name=first_name,
#                     last_name=last_name,
#                     username=username,
#                     email=email,
#                     profile_pic=profile_pic,
#                     user_type=3,
#                 )
#                 user.set_password(password)
#                 user.save()
#
#                 course = Courses.objects.get(id=course_id)
#                 # student.course_id = course
#
#                 session_year = SessionYearModel.objects.get(id=session_year_id)
#                 # student.session_year_id = session_year
#
#                 student = Students(
#                     admin=user,
#                     address=address,
#                     session_year_id=session_year_id,
#                     course_id=course,
#                     gender=gender
#                 )
#                 student.save()
#                 messages.success(request, user.first_name + " " + user.last_name + " are successfully added!")
#                 # messages.success(request, "Student Added Successfully!")
#                 return redirect('HOD_app:add_student')
#
#
#
#         context = {
#             'course': course,
#             'session_year': session_year,
#         }
#
#
#         return render(request, "HOD_template/add_student.html", context)


class ViewStudentView(View):
    def get(self, request):
        student = Students.objects.all()

        context = {
            'student': student,
        }

        return render(request, "HOD_template/view_student.html", context)


class EditStudentView(View):
    def get(self, request, id):
        student = Students.objects.filter(id=id)

        context = {
            'student': student
        }


        return render(request, "HOD_template/edit_student.html", context)