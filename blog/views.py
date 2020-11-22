from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm
from django.core.paginator import (
   Paginator, EmptyPage,
   PageNotAnInteger
)

def about(request):
    return render(request, "about.html")

def blog_index(request):
    object_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(object_list, 12) # 12 posts in each page
    page = request.GET.get('page')
    try:
       posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    # return render(request,
    #                 'blog/post_list.html',
    #                 {'page': page,
    #                 'posts': posts})
    context = {
        "page": page,
        "posts": posts
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context) 

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
        else: 
            form = CommentForm()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)