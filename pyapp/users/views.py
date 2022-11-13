from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse


from .forms import UserRegistrationForm, UserLoginForm
from .decorators import anonymous_user_required
from django.views import View


@anonymous_user_required
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                auth_login(request, user)
                return redirect(reverse("users:homepage"))

        else:
            for error in form.errors.values():
                messages.error(request, error)

    else:
        form = UserLoginForm()

    return render(request=request, template_name="users/login.html", context={"form": form})


def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect(reverse("users:homepage"))


@anonymous_user_required
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for registering!")
            return redirect("/")

        for error in form.errors.values():
            messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request=request, template_name="users/register.html", context={"form": form})


def homepage(request):
    """
    Renders the homepage for all users ( anonymous or logged in )
    """
    return render(request=request, template_name="users/homepage.html", context={"user": request.user})


class SecretAreaView(View):
    """
    class based views for cleaner code and better organization

    """

    def get(self, request):
        return render(request=request, template_name="users/secret_area.html", context={"user": request.user})


# mini hack since it doesn't work as a decorator for Class based views
# can also probably create a custom decorator for this
secret_area_view = login_required(SecretAreaView.as_view())
