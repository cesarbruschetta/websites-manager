from django.conf.urls import url

from websites_manager.core.views import file_serve, home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^files/(?P<path_slug>[\w]+)/(?P<path_name>.*)', file_serve, name='file_serve'),
]
