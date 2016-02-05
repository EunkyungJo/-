from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User
# 이런 식 별로 안 좋음. 아래처럼.
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.email import send_mail
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='약관동의', 
        error_messages={
            'required': '약관동의를 해주셔야 가입이 됩니다.',
    })

    class Meta(UserCreationForm.Meta):
        # fields = ['username', 'email']
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('중복된 이메일')
        return email


'''
class SignupForm2(UserCreationForm):
    email = forms.EmailField()
    # modelForm과 관련이 있는 것이 아니라, 장고 form과 관련. form은 db와는 관련이 없음. 받을 수는 있지만 저장은 하지 않음. 

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
'''

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('땡~~!')
        return answer


def send_signup_confirm_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)

    context = { 
            'user': user,
            'host': request.scheme + '://' + request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user),
        }

    subject = render_to_string('accounts.signup_confirm_subject.txt', context).splitlines()[0]
    body = render_to_string('accounts/signup_confirm_body.txt', context)
    to_email = [user.email]

    send_email(subject, body, None, to_email, fail_silently=False)
