from django.urls import path, include
from scrapper.views import PageListApiView, PageDetailApiView

urlpatterns = [
    path('', PageListApiView.as_view()),
    path('<str:page_id>/', PageDetailApiView.as_view()),
]
