from django.shortcuts import render

# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Tự đăng nhập
            return redirect('home')  # Chuyển về trang chủ
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



# Create your views here.
