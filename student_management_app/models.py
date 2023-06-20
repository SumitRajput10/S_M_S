from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from HOD_app.models import AdminHOD
from Staff_app.models import Staffs
from Student_app.models import Students



class SessionYearModel(models.Model):
    session_start_year = models.DateField()
    session_end_year = models.DateField()



# Overriding the Default Django Auth User and adding One More Field (user_type)
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, "HOD"),
        (2, "Staff"),
        (3, "Student"),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default=1, max_length=10)
    # profile_pic = models.ImageField(upload_to='media/profile_pic')


class Courses(models.Model):
    course_name = models.CharField(max_length=255)


class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='subjects')
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subjects')


class Attendance(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING, related_name='attendances')
    attendance_date = models.DateField()
    session_year = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)


class AttendanceReport(models.Model):
    # Individual Student Attendance
    student = models.ForeignKey("Student_app.Students", on_delete=models.DO_NOTHING, related_name='attendance_reports')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class LeaveReportStudent(models.Model):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)


class LeaveReportStaff(models.Model):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)


class FeedBackStudent(models.Model):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()


class FeedBackStaffs(models.Model):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()


class NotificationStudent(models.Model):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    message = models.TextField()


class NotificationStaffs(models.Model):
    staff = models.ForeignKey("Staff_app.Staffs", on_delete=models.CASCADE)
    message = models.TextField()


class StudentResult(models.Model):
    student = models.ForeignKey("Student_app.Students", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)


#Creating Django Signals
# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted) or else
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        elif instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        elif instance.user_type == 3:
            Students.objects.create(admin=instance)
    else:
        # Check the user_type and save the data in respective tables
        if instance.user_type == 1:
            instance.adminhod.save()
        elif instance.user_type == 2:
            instance.staffs.save()
        elif instance.user_type == 3:
            instance.students.save()