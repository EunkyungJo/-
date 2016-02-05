from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from blog.models import Post, About_us, Company, Member, Comment
from blog.forms import PostForm, CommentForm
from django.http import Http404

def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    params = {'post_list': post_list}
    return render(request, 'blog/post_list.html', params)


'''

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    params = {'post': post}
    return render(request, 'blog/post_detail.html', params)
DetailView: 일반적인 5대 뷰 중에서 하나이므로 generic으로 정의되어 있음.
모델만 지정해주면 이렇게 사용할 수 있게 되는 것.

일반적인 것들에 대해서는 CBV를 사용하면 코드 길이가 줄어듦.
아닌 경우에만 FBV를 사용해서 따로 정의한 함수를 사용.
CBV를 사용하면 OOP식으로 구조화를 시킬 수도 있음.

특정 부분의 코드 재정의
장고에서 PostDetailView클래스의 필요한 부분을 재정의하는 것. 직접 코드를 확인하는 것이 빠름.
'''

class PostDetailView(DetailView):
    def get_object(self, queryset=None):
        # self.kwargs:year, month, day, pk
        # self.kwargs:['year']
        '''
        try:
            return Post.objects.get(pk=self.kwargs['pk'])
        except PostDoesNotExist:
            raise Http404 # raise: 예외를 강제로 발생시킴.
        '''
        return get_object_or_404(Post, pk=self.kwargs['pk'])




'''
이걸 이용할 때는
아래의 코드를 사용.
'''
post_detail = PostDetailView.as_view()




#post_detail = DetailView.as_view(model=Post)
# django에서 form을 쓰는 일반적인 코드.

from django.contrib.auth.decorators import login_required
@login_required
def post_new(request):
    # print(request.GET)
    # print(request.POST)
    # print(request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog,.post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        })


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog,.post_detail', post.pk)  # 여기에서 views로 redirect를 시키다가, 이런 view가 없으면 이것이 view가 아닌 것으로 간주하고 뒤 이어지는 post.pk를 인자로 받지 않게 됨.
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
        })


def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            messages.debug(request, '새로운 댓글을 등록했습니다.') # request를 받으므로 view 내에서만 쓸 수 있음.
            return redirect('blog,.post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form,
    })


def comment_edit(request, post_pk, pk):
    # comment = Comment.objects.get(pk=pk)
    comment = Comment.get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog,.post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form,
    })


# get_objects.get() -> get_object_or_404로 바꾸기.
# 서버 문제가 아닌 경우 서버 문제가 아닌 것을 확실하게 하기 위해서.



def bio(request):
    return render(request, 'blog/bio.html')


def about_us(request):
    about_us = About_us.objects.all()
    return render(request, 'blog/about_us.html', {'about_us': about_us})


def members(request):
    members = Member.objects.all()
    return render(request, 'blog/members.html', {'members': members})


def companies(request):
    companies = Company.objects.all()
    return render(request, 'blog/companies.html', {'companies': companies})


def about_us_detail(request, pk):
    we = About_us.objects.get(pk=pk)
    return render(request, 'blog/about_us_detail.html', {'we': we})


# about_us_detail = DetailView.as_view(model=About_us)
# 이거 이용하면 안 나옴.. 왜 ???

member_detail = DetailView.as_view(model=Member)
company_detail = DetailView.as_view(model=Company)

