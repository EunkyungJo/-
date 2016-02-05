from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    is_agree = forms.BooleanField(label='약관동의',
    error_messages = {'required': '약관에 동의해주셔야, 서비스 이용이 가능합니다.'})

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' # 이렇게 명시해두었기 때문에 댓글을 달 때 모든 포스트 중에서 선택하라는 항목이 나오게 됨.
        fields = ['message'] # 특정 메시지의 한정. ('message', ) 혹은 ['message']. ,가 있느냐 없느냐에 따라서 tuple이냐 우선순위 연산자냐가 달라짐. 리스트는 문법이 유일하기 때문에 상관없음.