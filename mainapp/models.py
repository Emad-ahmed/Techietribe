from django.db import models

# Create your models here.


class Student(models.Model):
    id_no = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

    @staticmethod
    def get_student_by_id(id_no):
        try:
            return Student.objects.get(id_no=id_no)
        except:
            return False

    def __str__(self):
        return str(self.id_no)
