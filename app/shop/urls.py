from django.urls import include, path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
	path('futures', views.futures, name='futures'),
    path('', views.index, name='index'),
]