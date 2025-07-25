from django.contrib import admin
from django.urls import path
from .views import about_page, blog_page, details_page, home_page

urlpatterns = [
    path("", home_page, name="home_page" ),
    path("about/", about_page, name="about_page" ),
    path("blog/", blog_page, name="blog_page" ),
    path("blog/<int:blogid>", details_page, name="details_page" ),

    # path  viewname name
]