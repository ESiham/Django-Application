
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from ayomi_test.forms import CustomUserCreationForm, UserChangeForm

def dashboard(request):
    return render(request, "ayomi_test/dashboard.html")

def loginpage(request):
    return render(request, "registration/login.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "ayomi_test/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def editprofile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editprofile')
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'ayomi_test/editprofile.html', context)