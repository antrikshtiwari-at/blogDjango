from django.shortcuts import get_object_or_404, render

from blog.models import Blog

def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")


def blog_page(request):
    blogs = Blog.objects.all()
    return render(request, "blog.html", {"allblogs": blogs})



def details_page(request,blogid):
    blogdetails = get_object_or_404(Blog, pk=blogid )
    return render(request, "details.html", {"details":blogdetails }) 



def contact_us_page(request):
    return render(request, "contact_us.html")