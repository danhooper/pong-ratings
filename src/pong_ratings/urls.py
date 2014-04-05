'''
Main urls.
'''
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns(
    "",
    url(r"^$", login_required(TemplateView.as_view(template_name='homepage.html'))),
    url(r"^pong_ratings/$", login_required(TemplateView.as_view(template_name='homepage.html')),
                                    name="home"),
    url(r"^pong_ratings/admin/", include(admin.site.urls)),
    url(r'^pong_ratings/accounts/', include('account.urls')),
    url(r'^pong_ratings/score/', include('apps.score.urls')),
)


if settings.SERVE_MEDIA:
    urlpatterns += static(settings.STATIC_URL,
                          docuemnt_root=settings.STATIC_ROOT)
