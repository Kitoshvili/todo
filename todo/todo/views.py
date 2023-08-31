from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'templates/user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templates:user_list')
    else:
        form = UserForm()
    return render(request, 'templates/create_user.html', {'form': form})

def view_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'templates/view_user.html', {'user': user})

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:view_user', user_id=user_id)
    return render(request, 'templates/update_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('templates:user_list')
    return render(request, 'templates/delete_user.html', {'user': user})