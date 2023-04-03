from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scrapper.models import Page
from scrapper.serializers import PageSerializer


class PageListApiView(APIView):

    def get(self, request, *args, **kwargs):
        pages = Page.objects.order_by("-created_at")
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

class PageDetailApiView(APIView):

    def get_object(self, page_id):
        try:
            return Page.objects.get(uuid=page_id)
        except Page.DoesNotExist:
            return None

    def get(self, request, page_id, *args, **kwargs):
        page_instance = self.get_object(page_id)

        if not page_instance:
            return Response(
                {"error": "Page details not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PageSerializer(page_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, page_id, *args, **kwargs):
        page_instance = self.get_object(page_id)

        if not page_instance:
            return Response(
                {"error": "Page details not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = {
            "title": request.data.get("title"),
            "links": request.data.get("links"),
            "status": "done"
        }
        serializer = PageSerializer(
            instance=page_instance, data=data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
