from rest_framework import serializers
from scrapper.models import Page, PageLink


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ["uuid", "name", "total_links"]

