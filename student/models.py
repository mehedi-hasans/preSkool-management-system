from django.db import models

from authentication.models import customUser

# Create your models here.
class courseModel(models.Model):
    name=models.CharField(max_length=100)
    createat=models.DateTimeField(auto_now_add=True)
    updateat=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class sessionYearModel(models.Model):
    sessionStart=models.CharField(max_length=100)
    sessionEnd=models.CharField(max_length=100)
    def __str__(self):
        return self.sessionStart + " - " + self.sessionEnd
  
class studentModel(models.Model):
    admin = models.OneToOneField(customUser , on_delete=models.CASCADE)
    address=models.TextField()
    gender = models.CharField(max_length=100)
    courseid = models.ForeignKey(courseModel, on_delete=models.DO_NOTHING,default=1)  # Set the default course
    sessionyearid = models.ForeignKey(sessionYearModel, on_delete=models.DO_NOTHING,default=1)
    cratedat = models.DateTimeField(auto_now_add=True)  # Set the default value using timezone.now
    updateat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name