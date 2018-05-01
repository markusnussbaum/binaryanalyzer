from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from src.apps.main import views

urlpatterns = [
    url(r'^$', views.HomepageView.as_view()),
]
