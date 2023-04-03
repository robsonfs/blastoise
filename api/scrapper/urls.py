from django.urls import path, include
from scrapper.views import PageListApiView

urlpatterns = [
    path('', PageListApiView.as_view()),
]
