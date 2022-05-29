from multiprocessing.spawn import old_main_modules
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from mainApp.openFace import OpenFaceClient
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
from django.conf import settings
import os
from django.contrib.auth import authenticate
from .utils import base64_file

class FaceBackendAuthenication(ModelBackend):
 

    def faceAuthenicate(self,face_id,upload_face_id):
        
            
            faceResponse = OpenFaceClient().compareTwoFacesByImages(face_id,upload_face_id)
            os.remove(upload_face_id)
            confidence = faceResponse['confidence']
            print(confidence)
            if(confidence<80):
                return False
            return True

            
            
    

    def faceAuthenicateByImageBase(self,user_form):
        
            username = user_form.get('username')
            image_base64 = user_form.get('image_data_base64')
            user = User.objects.get(username=username)
            old_user_file = settings.MEDIA_ROOT + user.userfaceimage.image.name
            print(old_user_file)
            # path = default_storage.save(str(uuid.uuid1()) + '.jpg', ContentFile(image_file.read()))
            faceResponse = OpenFaceClient().compareTwoFacesByImageAndbase64(old_user_file,image_base64)
            confidence = faceResponse['confidence']
            print(confidence)
            if(confidence<80):
                print("photo do not match")
                raise Exception("photo do not match")

            authenticate(username=username, password=user.password)
            return user

