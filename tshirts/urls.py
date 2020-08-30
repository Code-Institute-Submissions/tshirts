from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from newin import urls as urls_newin
from about import urls as urls_about
from accounts import urls as urls_profile
from cart import urls as urls_cart


from checkout import urls as urls_checkout
from products.views import all_products
from newin.views import all_newin
from django.views import static
from .settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'), 
    url(r'^accounts/', include(urls_accounts)),
     url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),  
    url(r'^newin/', include(urls_newin)), 
    url(r'^about/', include(urls_about)),
    url(r'^checkout/', include(urls_checkout)),
   url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]