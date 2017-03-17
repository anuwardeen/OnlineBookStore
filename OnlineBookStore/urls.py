from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^top-authors-and-their-works/$', views.top_authors_and_works, name="top-authors-and-their-works"),
    url(r'^top-authors-and-their-works/rest/$', views.top_authors_and_works_rest, name="top-authors-and-their-works-rest"),
]
