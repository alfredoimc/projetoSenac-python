from django.conf.urls import include, url
from django.contrib import admin


from ccn.core import urls as core_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'ccn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', include(core_urls, namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
