from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationFormWithEmail


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationFormWithEmail()
    else:
        # Process completed form.
        form = UserCreationFormWithEmail(data=request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("users:login")
    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)
