from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            # Optionally, log the user in after registration
            login(request, user)
            return redirect('login')  # Redirect to login page or another page
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

    
# Profile view for both students and therapists/instructors
@login_required
def profile_view(request):
    user_profile = Profile.objects.get(user=request.user)
    # Show profile details based on user type
    return render(request, 'accounts/profile_view.html', {'user_profile': user_profile})

# Profile update view for therapists/instructors
@login_required
def profile_update(request):
    user_profile = Profile.objects.get(user=request.user)
    
    # Allow updating only if the user is a therapist or instructor
    if user_profile.is_therapist or user_profile.is_instructor:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=user_profile)
        return render(request, 'accounts/profile_update.html', {'form': form})
    else:
        # If the user is a student, redirect to a different page
        return redirect('home')