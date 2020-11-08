from django.conf.urls import url, include
from ayomi_test.views import dashboard, register, editprofile, loginpage
from django.urls import path

urlpatterns = [
    path('', loginpage, name='loginpage'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^editprofile/", editprofile, name='editprofile'),

]