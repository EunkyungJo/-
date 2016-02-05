from django.conf.urls import url
from django.http import JsonResponse
from blog.models import Post


def json_response(request, queryset):
    mylist = []
    for instance in queryset:
        mylist.append(instance.as_dict())
        return JsonResponse(mylist, safe=False)


def post_list(request):
    return json_response(request, Post.objects.all())


def post_list2(request):

