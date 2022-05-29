from django.urls import path
from django.conf.urls.static import static
from .import views
from .views import UserRegistration, user_login, verify_username , UserFaceLogin
urlpatterns = [
    # path('', views.index),
    path('welcome' , views.welcome),
    path('userRegister',UserRegistration.as_view(), name = 'register'),
    path('face_login',UserFaceLogin.as_view(), name='face_sign_in'), #API
    path('login', user_login, name='user_login'), #API
    path('verify/username', verify_username, name='verify_username') #API

]
