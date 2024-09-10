from django.db import models
from django.contrib.auth.models import User
from utils.fileutils import get_user_directory_path
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=get_user_directory_path, null=
                                      True, blank=True)
    
    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'