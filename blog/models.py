from django import forms
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator
from pr.utils import random_name_upload_to
import re

'''
def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message='휴대폰 번호를 입력해주세요.')(number)


class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):

        #if 'max_length' not in kwargs:
        #    kwargs['max_length']=11
        #    이 코드를 아래처럼 한 줄로

        kwargs.setdefault('max_length', 15)
        super(PhoneField, self).__init__(*args, **kwargs)
        validator = RegexValidator(r'^01[016789]\d{7,8}$',
            message='휴대폰 번호를 입력해주세요.')
        self.validators.append(phone_validator)
'''


def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    if not re.match(r'^01[016789]\d{7,8}$', number):
        raise forms.ValidationError("휴대폰 번호를 입력해주세요.")


class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(phone_validator)


def min_length_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하세요.')


class Post(models.Model):
    title = models.CharField(max_length=100,
        validators=[min_length_validator],
        help_text='포스팅 제목을 100자 이내로 써주세요.')
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=random_name_upload_to)
    # 파일의 경로를 저장함 -> blank=True조건을 없앴을 때 default를 저장하라는 조건이 뜨면 문자열을 줘야함. ""이런 식으로.
    phone = PhoneField(blank=True)
    # tag = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    # 밑에 있어도 문자열로 'Tag'라고 써 주면 현재 모듈 안에 있는 클래스라는 사실의 전달. 다른 앱일 경우는 'auth.User'이런 식으로 전달. 아니면 import한 다음에 지정할 수도 있음.
    # blank=True가 안 되어 있으면, 태그가 하나 이상 반드시 지정되어 있어야 save가 되는 것.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

def 

@python_2_unicode_compatible
# python2에서도 __str__이 사용 가능하도록. python2에는 __unicode__로 되어 있음.
class Member(models.Model):
    name = models.CharField(max_length=10)
    intro = models.TextField()
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    career = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=20)
    intro = models.TextField()
    year = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    detail = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class About_us(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=20)
    intro = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post,)
    message = models.TextField()

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
