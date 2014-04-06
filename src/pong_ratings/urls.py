'''
Main urls.
'''
# pylint: disable=invalid-name
# pylint: disable=no-value-for-parameter
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from pong_ratings.apps.score import views
admin.autodiscover()

handler500 = "pinax.views.server_error"


urlpatterns = patterns(
    "",
    url(r"^$",
        RedirectView.as_view(url='/%s/score/handicap/' % settings.SITE_ROOT),
        name='site_root'),
    url(r"^%s/$" % settings.SITE_ROOT,
        RedirectView.as_view(url='/%s/score/handicap/' % settings.SITE_ROOT),
        name='home'),
    url(r"^%s/admin/" % settings.SITE_ROOT, include(admin.site.urls)),
    url(r"^%s/accounts/signup/$" % settings.SITE_ROOT,
        views.SignupView.as_view(),
        name="account_signup"),
    url(r'^%s/accounts/' % settings.SITE_ROOT,
        include('account.urls')),
    url(r'^%s/score/' % settings.SITE_ROOT,
        include('apps.score.urls')),
)


if settings.SERVE_MEDIA:
    urlpatterns += static(settings.STATIC_URL,
                          docuemnt_root=settings.STATIC_ROOT)
