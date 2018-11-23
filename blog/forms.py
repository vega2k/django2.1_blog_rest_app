from django import forms
from blog.models import Post

#length check를 하는 함수 정의
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해 주세요')

# 1. Form 을 상속받는 PostForm 클래스 선언
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)

#2. ModelForm 을 상속 받는 PostModelForm 클래스 선언
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']