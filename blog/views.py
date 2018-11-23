from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import PostForm, PostModelForm
from blog.models import Post

#Post 목록조회
def post_list(request):
    # myname = 'Django'
    # return HttpResponse('''<h1>Hello {name}</h1>
    # '''.format(name=myname))
    posts = Post.objects.filter(published_date__lte=timezone.now()).\
        order_by('published_date')
    return render(request,'blog/post_list.html',{'posts_key':posts})

#Post 상세조회
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

#Post 등록 : PostForm 사용
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        #검증 ok
        if form.is_valid():
            print(form.cleaned_data)
            #row가 등록처리 됨
            post = Post.objects.create(
                author=request.user,
                title=form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                published_date = timezone.now())
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_form.html',{'form':form})

#Post 등록 : PostModelForm 사용
@login_required
def post_new_modelform(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        #검증 ok
        if form.is_valid():
            print(form.cleaned_data)
            #row가 등록처리 됨
            post = form.save(commit=False)
            print(post)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostModelForm()
    return render(request,'blog/post_form.html',{'form':form})

#Post 수정 : PostModelForm 사용
@login_required
def post_edit(request,pk):
    #pk에 해당되는 post 객체 가져오기
    post = get_object_or_404(Post,pk=pk)
    print(post)
    if request.method == 'POST':
        form = PostModelForm(request.POST,instance=post)
        #검증 ok
        if form.is_valid():
            print(form.cleaned_data)
            #row가 수정처리 됨
            post = form.save(commit=False)
            print(post)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request,'blog/post_form.html',{'form':form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')