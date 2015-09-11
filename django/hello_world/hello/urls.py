from django.conf.urls import include, url
from hello import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^corgi.html', views.awesome, name='awesome'),
    url(r'^forum', views.forum, name='forum'),
]