
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from movies.forms import CustomUserCreationForm, UserInfoForm


# def register(request):
#     """Register a new user"""
#     if request.method != 'POST':
#         #Display blank form
#         form = CustomUserCreationForm()
#     else:
#         # Process the completed form
#         form = CustomUserCreationForm(data=request.POST)

#         if form.is_valid:
#             new_user = form.save()

#             #Login the user in and redirect to home page

#             login(request, new_user)
#             return redirect('movies:index')

#     # Display Form filled or invalid
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank form
        form = CustomUserCreationForm()
        user_info_form = UserInfoForm()
    else:
        # Process the completed form
        form = CustomUserCreationForm(data=request.POST)
        user_info_form = UserInfoForm(request.POST, request.FILES or None)

        if form.is_valid and user_info_form.is_valid():
            new_user = form.save()

            profile = user_info_form.save(commit=False)
            profile.user = new_user
            profile.save()            

            #Login the user in and redirect to home page

            login(request,new_user)
            return redirect('movies:index')

    # Display Form filled or invalid
    context = {'form': form, 'user_info_form': user_info_form}
    return render(request, 'registration/register.html', context)