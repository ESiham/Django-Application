from django.conf.urls import url, include
from ayomi_test.views import dashboard, register, editprofile

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^editprofile/", editprofile, name='editprofile'),

]