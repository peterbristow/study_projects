from django.conf.urls import url
from django.contrib import admin

import posts.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts.views.home, name="home"),
    url(r'^sort/(?P<sort_by>[a-z]{2})/$', posts.views.sort, name="sort"),
    url(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.post_detail, name="post_detail"),
]
