from django.urls import path
from .views import home_view, blog_view, about_view, blog_single_view, contact_view, category_view

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view, name='blog'),
    path('blog_single/<int:post_id>/', blog_single_view, name='blog_single'),
    path('category/', category_view, name='category'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),

]
