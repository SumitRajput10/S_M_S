from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from HOD_app.models import AdminHOD
from Staff_app.models import Staffs
from Student_app.models import Students





# Overriding the Default Django Auth User and adding One More Field (user_type)
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class SessionYearModel(models.Model):
    session_start_year = models.DateField()
    session_end_year = models.DateField()

    def __str__(self):
        return f"{self.session_start_year} To {self.session_end_year}"


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, "HOD"),
        (2, "Staff"),
        (3, "Student"),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default=1, max_length=10)
    profile_pic = models.ImageField(upload_to='media/profile_pic', default="{% url static '/assets/img/profiles/default_avatar.jpg' %}")


class Courses(Common):
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name



class Subjects(Common):
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='subjects')
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.subject_name

class Attendance(Common):
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING, related_name='attendances')
    attendance_date = models.DateField()
    session_year = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.subject_name

class AttendanceReport(Common):
    # Individual Student Attendance
    student = models.ForeignKey("Student_app.Students", on_delete=models.DO_NOTHING, related_name='attendance_reports')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.admin.first_name


class LeaveReportStudent(Common):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)

    def __str__(self):
        return self.student.admin.first_name + " " + self.student.admin.last_name


class LeaveReportStaff(Common):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)

    def __str__(self):
        return self.staff.admin.first_name + " " + self.staff.admin.last_name


class FeedBackStudent(Common):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.student.admin.first_name + " " + self.student.admin.last_name



class FeedBackStaffs(Common):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.staff.admin.first_name + " " + self.staff.admin.last_name


class NotificationStudent(Common):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.student.admin.first_name

class NotificationStaffs(Common):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.staff.admin.first_name


class StudentResult(Common):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)

    def __str__(self):
        return self.student.admin.first_name + " " + self.student.admin.last_name

#
# #Creating Django Signals
# # It's like trigger in database. It will run only when Data is Added in CustomUser model
#
# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will automatically insert data in HOD, Staff or Student
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted) or else
#     if created:
#         # Check the user_type and insert the data in respective tables
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         elif instance.user_type == 2:
#             Staffs.objects.create(admin=instance)
#         elif instance.user_type == 3:
#             Students.objects.create(admin=instance)
#     else:
#         # Check the user_type and save the data in respective tables
#         if instance.user_type == 1:
#             instance.adminhod.save()
#         elif instance.user_type == 2:
#             instance.staffs.save()
#         elif instance.user_type == 3:
#             instance.students.save()