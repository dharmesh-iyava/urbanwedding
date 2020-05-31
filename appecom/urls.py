from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('caterer/', views.homeView.as_view(), name='caterer'),
    path('caterer/caterer_list/<slug>/',
         views.catererView.as_view(), name='catererproduct')
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
