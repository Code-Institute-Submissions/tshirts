from django.conf.urls import url, include
from .views import all_newin

urlpatterns = [
    url(r'^$', all_newin, name='newin'),
]