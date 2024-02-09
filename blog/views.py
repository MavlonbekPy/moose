from .models import Post, Contact, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator


def home_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts
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
        'posts': page_obj.page(page)
    }

    return render(request, 'blog.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def blog_single_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog_single.html', context)


def category_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        posts = Post.objects.filter(category__name=selected_category)
    else:
        posts = Post.objects.all()

    return render(request, 'category_view.html', {'posts': posts, 'categories': categories})


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'), subject=data.get('subject'),
                                     message=data.get('message'))
        obj.save()
        return redirect('/contact/')
    return render(request, 'contact.html')
