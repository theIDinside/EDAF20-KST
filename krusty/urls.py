from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from home.views import error400, error403, error404, error500

urlpatterns = i18n_patterns(
    url(r'^', include('home.urls')),
)

handler400 = error403
handler403 = error403
handler404 = error404
handler500 = error500
