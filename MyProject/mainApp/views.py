
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from mainApp.authenticate import FaceBackendAuthenication
from django.contrib.auth.models import User
# # creating some global variables
# us = ''
# em = ''
# pswd = ''
# usL = ''
# pswdL = ''

# # Create your views here.
# def index(request):
#     return render(request , 'first.html')

def welcome(request):
    return render(request , 'welcome.html')

# def faceSignUpSystem(request):
#     global us , em , pswd
#     if request.method=="POST":
#         m=sql.connect(host='localhost' , user='root' , password='mysql' , database='srajan')
#         cursor = m.cursor()
#         d=request.POST
#         for key , value in d.items():
#             if key=="user_name":
#                 us = value
#             if key=="email":
#                 em = value
#             if key=="password":
#                 pswd = value
#         c = "insert into one Values('{}','{}','{}')".format(us,em,pswd)
#         cursor.execute(c)
#         m.commit()
#     return render(request , 'signup_page.html')

# def faceLoginSystem(request):
#     global usL , pswdL
#     if request.method == "POST":
#         m=sql.connect(host='localhost' , user='root' ,password='mysql' , database='srajan')
#         cursor = m.cursor()
#         d=request.POST
#         for key ,value in d.items():
#             if key=="user_name":
#                 usL = value
#             if key=="password":
#                 pswdL = value
#         c = "select * from one where user_name='{}' and password='{}'".format(usL , pswdL)
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             return render (request , 'error.html')
#         else:
#             return render(request , 'welcome.html')
#     return render(request , 'login_page.html')


# class UserSignUpView(View):

#     def post(self, request):

#         try:
#             username = request.POST.get("username")
#             password = request.POST.get("password")
#             email = request.POST.get("email")
#             newUser = User(email=email, username=username)

#             newUser.set_password(password)
#             newUser.save()
#             user = authenticate(username=username,password=password)
#             login(user)
#             # return render(request , 'welcome.html')
#             return JsonResponse({
#                 "message": "Created successfully",
#                 "user": newUser.to_json()
#             })
#         except Exception as e:
#             print(e)
#             return render(request, 'error.html')

class UserRegistration(View):
# this takes the username, password, email and a image for user sign up
    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self, request):
        form = UserCreationForm(request.POST, request.FILES)
        

    
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            # user = authenticate(username=username, password=password)
            # login( request,user)
            return JsonResponse({
                "sucess":"true",
                'data': "successfull login"
            })
        else: 
            print(form.errors)
            return JsonResponse({
                "sucess"
                'data': form.errors
            })
       


class UserFaceLogin(View):
    def post(self,request):
       
        
        # print(request.FILES)
       

        try:
            form = request.POST
            oldUser = FaceBackendAuthenication().faceAuthenicateByImageBase(form)
            login(request, oldUser)

            return JsonResponse({
                "sucess" :"true",
                'data': "successfull login"
            })
        except Exception as e:
            return JsonResponse({
                "sucess":"false",
                'data': str(e)
            })

        # return JsonResponse({

        # })






def user_login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    else :
        return JsonResponse({
            "message": "post login"
        })

def verify_username(request):
    user = User.objects.filter(username=request.POST['user_name'])
    if user:
        return JsonResponse({
            'isValid': True
        })
    else:
        return JsonResponse({
            'isValid': False
        })