from django.conf.urls import url, include
from django.contrib import admin
from mapsite.views import IndexView, upload_data


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^upload/', upload_data, name='upload'),
    url(r'^upload/map', upload_data, name='map')
]
