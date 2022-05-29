from django.db import models
from django.contrib.auth.models import User
import os
import time

def content_file_name(instance, filename):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    name, extension = os.path.splitext(filename)
    return os.path.join('content', "hello", timestr + extension)

class UserFaceImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to=content_file_name, blank=False)


    def createUserFaceImage(user, image):
        my_user = UserFaceImage(image = image)
        my_user.user = user
        my_user.save()


 







