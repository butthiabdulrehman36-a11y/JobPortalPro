from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:dashboard")

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


def logout_view(request):
    logout(request)
    return redirect("core:home")


def register(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("accounts:dashboard")

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")
