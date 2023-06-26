from django.db import models



class Students(models.Model):
    admin = models.OneToOneField("student_management_app.CustomUser", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    course_id = models.ForeignKey("student_management_app.Courses", on_delete=models.DO_NOTHING, null=True)
    session_year_id = models.ForeignKey("student_management_app.SessionYearModel", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

