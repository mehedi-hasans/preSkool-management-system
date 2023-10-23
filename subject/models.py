from django.db import models

from student.models import courseModel
from teacher.models import teacherModel

# Create your models here.
class subjectModel(models.Model):
    name=models.CharField(max_length=100)
    course=models.ForeignKey(courseModel,on_delete=models.CASCADE)
    teacher=models.ForeignKey(teacherModel,on_delete=models.CASCADE)
    cratedat = models.DateTimeField(auto_now_add=True, null=True)  # Set the default value using timezone.now
    updateat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name