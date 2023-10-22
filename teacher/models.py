from django.db import models

from authentication.models import customUser
from student.models import courseModel

# Create your models here.
class teacherModel(models.Model):
    admin = models.OneToOneField(customUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender = models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    courseid = models.ForeignKey(courseModel, on_delete=models.DO_NOTHING,default=2)
    experience=models.CharField(max_length=100)
    cratedat = models.DateTimeField(auto_now_add=True)  # Set the default value using timezone.now
    updateat = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name