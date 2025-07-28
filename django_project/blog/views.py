from django.shortcuts import render

posts = [
    {
        "author": "Sib",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "July 27,  2025"
    },
    {
        "author": "Lisle",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "July 28,  2025"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "About"})