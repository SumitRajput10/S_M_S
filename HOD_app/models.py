from django.db import models


class AdminHOD(models.Model):
    admin = models.OneToOneField("student_management_app.CustomUser", on_delete=models.CASCADE)
    # department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Admin HOD"


class StudentFees(models.Model):
    student = models.ForeignKey("Student_app.Students", related_name= "studentfees", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # due_date = models.DateField()
    is_paid = models.BooleanField(default=False)


class StaffSalary(models.Model):
    staff = models.ForeignKey("Staff_app.Staffs", related_name='staffsalary', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Staff: {self.staff}, Amount: {self.amount}, Payment Date: {self.payment_date}, Is Paid: {self.is_paid}"


