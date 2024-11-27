from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import AvatarForm
from .models import Avatar, UserProfile, BehaviorLog
import openai

# OpenAI API Key (Replace with your actual API key)
openai.api_key = "your_openai_api_key"  # Replace with your API key


def home(request):
    """Render the home page."""
    return render(request, 'core/home.html')


def customize_avatar(request):
    """Handle avatar customization."""
    # Fetch or create the user's profile and avatar
    user_profile, created = UserProfile.objects.get_or_create(
        email="test@example.com", defaults={"name": "Test User"}
    )
    avatar = user_profile.avatar or Avatar.objects.create()

    if request.method == 'POST':
        form = AvatarForm(request.POST, instance=avatar)
        if form.is_valid():
            avatar = form.save(commit=False)
            # Save selected accessories as a list
            avatar.accessories = form.cleaned_data['accessories']
            avatar.save()
            user_profile.avatar = avatar
            user_profile.save()

            # Log the avatar customization action
            log_behavior(user_profile, "Avatar customization", {"avatar": avatar.id})

            return redirect('avatar_success')  # Redirect after saving
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'core/customize_avatar.html', {'form': form})


def avatar_success(request):
    """Render the success page after avatar customization."""
    return render(request, 'core/avatar_success.html')


def chatbot(request):
    """Chatbot integration using OpenAI."""
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"User: {user_message}\nBot:",
                max_tokens=100,
                temperature=0.7,
            )
            bot_message = response['choices'][0]['text'].strip()
            return JsonResponse({"message": bot_message})
        except Exception as e:
            return JsonResponse({"message": "Sorry, an error occurred."})
    return JsonResponse({"message": "Invalid request."})


def log_behavior(user, action, additional_data=None):
    """Log user behavior for analytics and recommendations."""
    additional_data = additional_data or {}
    BehaviorLog.objects.create(user=user, action=action, additional_data=additional_data)

def index(request):
    return render(request, 'core/index.html')
