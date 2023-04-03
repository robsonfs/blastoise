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

    def post(self, request, *args, **kwargs):
        data = {
            "url": request.data.get("url")
        }

        serializer = PageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
