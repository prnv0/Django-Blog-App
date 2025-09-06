from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Pranav S",
        "title" : "Blog Post 1",
        "date_posted": "September 6 2025",
        "content": "Content 1",
    },
    {
        "author": "John Doe",
        "title" : "Blog Post 2",
        "date_posted": "September 5 2025",
        "content": "Content 2",
    },
]
# Create your views here.
def home(request):
    context = {
        "posts": posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})