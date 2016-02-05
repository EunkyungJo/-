from django.conf import settings
# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm, SignupForm2
from django.contrib import messages
from django.contrib.auth import get_user_model, get_backends, login as auth_login
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.forms import send_signup_confirm_email

def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            user = form.save()
            backend_cls = get_backends()[0].__class__
            backend_path = backend_cls.__module__ + '.' + backend_cls.__name__
            user.backend = backend_path
            auth_login(request, user)
            messages.info(request, 'Welcome. ;)')
            return redirect(settings.LOGIN_REDIRECT_URL)
            
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # send_signup_confirm_email(request, user)
            # return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm2()
    return render(request, 'accounts/signup.html', {'form': form, })


def signup_confirm(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, '이메일을 인증했습니다. 로그인해주세요. ;)')
        return redirect(settings.LOGIN_URL)
    else:
        messages.error(request, '잘못된 경로로 접근하셨습니다. :-(')
        return redirect(settings.LOGIN_URL)
