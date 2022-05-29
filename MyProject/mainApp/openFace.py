from MyProject.settings import OPEN_FACE_CREDENTIAL
import requests

import json


class OpenFaceClient(object):

    def __init__(self):
            self.api_key = OPEN_FACE_CREDENTIAL['api_key']
            self.api_secret = OPEN_FACE_CREDENTIAL['api_secret']
            self.url = "https://api-us.faceplusplus.com/facepp/v3/compare"

    def compareTwoFacesByImages(self, images1, images2):
        from io import StringIO



        payload = {'api_key': self.api_key,
                   'api_secret': self.api_secret}
        # file_handle = StringIO(str(images1.read()))


        files = [
            ('image_file1',
             ('img1.jpg', open(images1, 'rb'), 'image/jpg')),
            ('image_file2', ('img2.jpg', open(images2, 'rb'), 'image/jpg'))
        ]
        headers = {}

        response = requests.request("POST", self.url, headers=headers, data=payload, files=files)

        return response.json()

    def compareTwoFacesByFaceToken(self, face_token, images2):
        payload = {'api_key': self.api_key, 'api_secret': self.api_secret, 'face_token1': face_token}
        files = [
            ('image_file2', ('file2.jpg', open(images2, 'rb'), 'image/jpeg'))
        ]

        headers = {}

        response = requests.request("POST", self.url, headers=headers, data=payload, files=files)

        return response.json()


    def compareTwoFacesByImageBase64(self,face_token, image_base):
            payload = {'api_key': self.api_key, 'api_secret': self.api_secret, 'face_token1': face_token, 'image_base64_2':image_base}
            headers = {}
            response = requests.request("POST", self.url, headers=headers, data=payload)

            return response.json()

    def compareTwoFacesByImageAndbase64(self,image_path, image_64):
        payload = {'api_key': self.api_key, 'api_secret': self.api_secret, 'image_base64_2':image_64}
        files = [
            ('image_file1', ('file1.jpg', open(image_path, 'rb'), 'image/jpeg'))
        ]
        headers = {}
        response = requests.request("POST", self.url, headers=headers, data=payload, files=files)

        return response.json()


