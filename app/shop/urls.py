from django.urls import include, path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
	path('futures', views.futures, name='futures'),
	path('purchases', views.purchases, name='purchases'),
	path('show_future/<int:pk>', views.show_future, name='show_future'),
	path('product/<int:pk>', views.product, name='product'),
	path('buy/<int:pk>', views.buy, name='buy'),
	path('future', views.future, name='future'),
    path('shop', views.shop, name='shop'),
    path('', views.index, name='index'),
]