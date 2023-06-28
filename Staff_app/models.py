from django.db import models




class Staffs(models.Model):
    admin = models.OneToOneField("student_management_app.CustomUser", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.admin.username