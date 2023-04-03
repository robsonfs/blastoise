from rest_framework import serializers
from .models import Page, PageLink


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ["uuid", "name", "total_links"]

