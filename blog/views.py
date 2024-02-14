from .models import Post, Contact, Category, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
import requests


def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('created_at')[:4]
    d = {
        'posts': posts,
        'home': 'active'
    }
    return render(request, 'index.html', context=d)


def blog_view(request):
    data = request.GET
    cat = data.get('cat')

    page = data.get('page', 1)

    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)

    page_obj = Paginator(posts, 2)

    d = {
        'posts': page_obj.page(page),
        'blog': 'active'
    }

    return render(request, 'blog.html', context=d)


def about_view(request):
    d = {
        'about': 'active'
    }
    return render(request, 'about.html', context=d)


def blog_single_view(request, post_id):
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=post_id, name=data['name'], email=data['email'], message=data['message'])
        obj.save()
        return redirect(f'/blog_single/{post_id}')
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)

    return render(request, 'blog_single.html', context={'post': post, 'comments': comments})


def category_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        posts = Post.objects.filter(category__name=selected_category)
    else:
        posts = Post.objects.all()

    return render(request, 'category_view.html', {'posts': posts, 'categories': categories}, )


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'), subject=data.get('subject'),
                                     message=data.get('message'))
        obj.save()
        """Telegram Notify"""
        token = "6749312297:AAHVOEH5pugcBZZt3aRaXwf8YgflvnQO6vg"
        requests.get(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id=5210463524&text=MOOSE\nid: {obj.id}\nname: {obj.name}\nemail: {obj.email}\nmessage: {obj.message}""")
        return redirect('/contact/')
    return render(request, 'contact.html',context={'contact': 'active'})
