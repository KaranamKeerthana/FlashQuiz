from django.urls import path
from testapp import views

urlpatterns=[
    path('display/',views.display,name="display"),
    path('create/',views.register,name="register"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),       
]