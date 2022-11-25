from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from users.forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Signed up successfully.")
            return redirect('item_list')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/sign_up.html', context)


class MyLoginView(SuccessMessageMixin, LoginView):    
    template_name = 'registration/login.html'
    success_url = ''
    success_message = "Logged in successfully."
    


def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('item_list')


class MyPasswordResetView(PasswordResetView):
    template_name = 'registration/reset_password.html'
    html_email_template_name: str = 'registration/reset_password_email.html'
    success_url = reverse_lazy('reset_password_sent')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('item_list')
        return super().dispatch(*args, **kwargs)


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/reset_password_sent.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('item_list')
        return super().dispatch(*args, **kwargs)


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_complete')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('item_list')
        return super().dispatch(*args, **kwargs)


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/reset_password_complete.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('change_password_complete')
    login_url = '/login/'


class MyPasswordChangeCompleteView(LoginRequiredMixin, PasswordResetCompleteView):
    template_name = 'registration/change_password_complete.html'
    login_url = '/login/'


@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'registration/profile.html', context)
