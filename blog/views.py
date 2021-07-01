import math
from django.shortcuts import render
from blog.models import Post, Comment, Category
from .forms import CommentForm
from django.core.paginator import (
   Paginator, EmptyPage,
   PageNotAnInteger
)
import os
import requests

def about(request):
    return render(request, "about.html", {})

def test(request):
    return render(request, "test.html")


def blog_index(request):
    object_list = Post.objects.all().order_by('-created_on')
    catList = Category.objects.all().order_by('-name')
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
    pagesCount = int(math.ceil(len(object_list)/12))
    context = {
        "page": page,
        "posts": posts,
        "postsLength": len(posts),
        "pagesCount": range(1,pagesCount+1),
        "categories": catList
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    catList = Category.objects.all().order_by('-name')
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts,
        "categories": catList
    }
    return render(request, "blog_category.html", context)

def grecaptcha_verify(request):
    data = request.POST
    captcha_rs = data.get('g-recaptcha-response')
    url = "https://www.google.com/recaptcha/api/siteverify"
    headers = {'User-Agent': 'DebuguearApi-Browser',}
    params = {'secret': os.environ['RECAPTCHA_PRIVATE_KEY'], 'response': captcha_rs}
    verify_rs = requests.post(url,params, headers=headers)
    verify_rs = verify_rs.json()
    response = verify_rs.get("success", False)
    return response

def blog_detail(request, pk):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    all_posts = Post.objects.all().order_by('-created_on')

    prevVal = None
    nextVal = None
    for i, item in enumerate(all_posts):
      if item.pk == pk:
          if (i > 0):
              prevVal = all_posts[i-1].pk
          if (i < len(all_posts)-1):
              nextVal = all_posts[i+1].pk

    post = Post.objects.get(pk=pk)
    new_comment = False
    tryToPost = False
    form = CommentForm()

    if request.method == 'POST':
        tryToPost = True
        print("IT IS A POST")
        response=grecaptcha_verify(request)
        if response == True :
            form = CommentForm(request.POST)
            if form.is_valid():

                comment = Comment(
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post
                )
                comment.save()
                new_comment = True
            else:
                form = CommentForm()
                print("Form is not valid")
        else:
            print("CAPTCHA IS FAILING")

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "new_comment": new_comment,
        "prevVal": prevVal,
        "nextVal": nextVal,
        "tryToPost": tryToPost
    }
    return render(request, "blog_detail.html", context)
