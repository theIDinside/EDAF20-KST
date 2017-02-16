from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from home.views import error400, error403, error404, error500
from krusty import settings

urlpatterns = i18n_patterns(
    url(r'^', include('home.urls')),
)


if settings.DEBUG:
    urlpatterns += i18n_patterns(
        url(r'^400/$', error400),
        url(r'^403/$', error403),
        url(r'^404/$', error404),
        url(r'^500/$', error500),
    )


handler400 = error403
handler403 = error403
handler404 = error404
handler500 = error500
