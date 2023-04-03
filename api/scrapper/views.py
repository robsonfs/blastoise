from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scrapper.models import Page, PageLink
from scrapper.serializers import PageSerializer


class PageListApiView(APIView):

    def get(self, request, *args, **kwargs):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
