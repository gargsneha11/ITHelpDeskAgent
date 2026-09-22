# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile


def signup(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        # Check existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect("signup")

        # Create Django user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        # Generate CampusIT user ID
        user_number = 1000 + user.id
        campus_user_id = f"USR-{user_number}"

        # Create profile
        UserProfile.objects.create(
            user=user,
            campus_user_id=campus_user_id
        )

        messages.success(
            request,
            f"Account created successfully! Your User ID is {campus_user_id}."
        )

        return redirect("login")

    return render(request, "accounts/signup.html")

from django.contrib.auth import authenticate, login, logout


def user_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        messages.error(request, "Invalid email or password.")
        return redirect("login")

    return render(request, "accounts/login.html")

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    profile = request.user.userprofile

    return render(
        request,
        "accounts/dashboard.html",
        {
            "name": request.user.first_name,
            "campus_user_id": profile.campus_user_id
        }
    )


from agent.campusit_agent import chat_with_agent
@login_required
def chat(request):

    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    if request.method == "POST":

        user_message = request.POST.get("message", "").strip()

        if user_message:

            previous_response_id = request.session.get(
                "previous_response_id"
            )

            user_id = request.user.userprofile.campus_user_id

            result = chat_with_agent(
                user_message=user_message,
                previous_response_id=previous_response_id,
                user_id=user_id
            )

            # Save the conversation in Django session
            chat_history = request.session["chat_history"]

            chat_history.append({
                "role": "user",
                "message": user_message
            })

            chat_history.append({
                "role": "agent",
                "message": result["message"]
            })

            request.session["chat_history"] = chat_history

            # Save Foundry conversation context
            request.session["previous_response_id"] = (
                result["response_id"]
            )

    return render(
        request,
        "accounts/chat.html",
        {
            "chat_history": request.session.get(
                "chat_history", []
            )
        }
    )

import json
from pathlib import Path

@login_required
def my_tickets(request):

    user_id = request.user.userprofile.campus_user_id

    tickets_file = Path("data/tickets.json")

    with open(tickets_file, "r") as file:
        data = json.load(file)

    user_tickets = [
        ticket
        for ticket in data["tickets"]
        if ticket["user_id"] == user_id
    ]

    return render(
        request,
        "accounts/my_tickets.html",
        {
            "tickets": user_tickets,
            "campus_user_id": user_id
        }
    )

@login_required
def service_status(request):

    services_file = Path("data/services.json")

    with open(services_file, "r") as file:
        data = json.load(file)

    return render(
        request,
        "accounts/service_status.html",
        {
            "services": data["services"]
        }
    )

@login_required
def profile(request):
    user = request.user
    profile = user.userprofile

    return render(
        request,
        "accounts/profile.html",
        {
            "name": user.first_name,
            "email": user.email,
            "campus_user_id": profile.campus_user_id,
        }
    )

from django.contrib.auth import authenticate, login, logout

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def new_chat(request):
    request.session["chat_history"] = []
    request.session.pop("previous_response_id", None)

    return redirect("chat")