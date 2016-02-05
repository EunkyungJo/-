from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bio/$', views.bio, name='bio'),

    url(r'^posts/new/$', views.post_new, name='newpost'),

    url(r'^posts/(?P<pk>\d+)/edit/$', views.post_edit, name='postedit'),
    url(r'^posts/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='newcomment'),
    url(r'^posts/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='editcomment'),



    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^about_us/(?P<pk>\d+)/$', views.about_us_detail, name='about_us_detail'),

    url(r'^members/$', views.memebers, name='members'),
    url(r'^members/(?P<pk>\d+)/$', views.member_detail, name='members_detail'),

    url(r'^companies/$', views.companies, name='companies'),
    url(r'^companies/(?P<pk>\d+)/$', views.company_detail, name='company_detail'),

]
