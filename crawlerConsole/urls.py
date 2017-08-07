from django.conf.urls import url
from crawlerConsole import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/', views.login_view,name='login'),
    url(r'^ajax/',views.startCommand),
    # url(r'^echo_once',views.echo_once),
]