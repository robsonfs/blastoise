import uuid

from django.db import models


class Page(models.Model):

    STATUS_CHOICES = (
        ("in_progress", "In progess..."),
        ("done", "Done"),
    )

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default="in_progress"
    )

    @property
    def name(self):
        return self.title or "page processing"

    @property
    def total_links(self):
        return self.links.get_queryset().count() or "in progress"

    def __str__(self):
        return self.title or self.url


class PageLink(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    href_attr = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    page = models.ForeignKey(
        "scrapper.Page", on_delete=models.CASCADE, related_name="links"
    )

    def __str__(self):
        return self.name

