from django.conf.urls import url, include  

urlpatterns = [
    url(r'^', include('apps.users_app.urls')),
    url(r'^', include('apps.blogs_app.urls')),
    url(r'^', include('apps.surveys_app.urls')),
]