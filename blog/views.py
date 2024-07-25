from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm

def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

class PostCreate(View):
    def get(self, request):
        form = PostForm
        return render(request, 'blog/post/post_create_form.html',
                {'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('/blog/')
        return render(request, 'blog/post/post_create_form.html',
                      {'form': bound_form})