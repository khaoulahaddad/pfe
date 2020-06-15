from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from suppervision.views import *
from django.contrib import admin
from django.urls import include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

admin.autodiscover()

urlpatterns =[
    # Examples:
    # url(r'^$', 'khaoula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', test_cookies),
    url(r'^home',login),
    url(r'^forgetpassword',forgetpassword),
    url(r'^search',search),
    url(r'^teste',teste),
    url(r'^resetpsw',resetpsw),
    url(r'^profil',profil),
    url(r'^confirm',confirm),
    url(r'^logout',logout),
    url(r'^alltask',alltask),
    url(r'^newtask',newtask),
    url(r'^currenttask',currenttask),
    url(r'^resolvedtask',resolvedtask),
]
