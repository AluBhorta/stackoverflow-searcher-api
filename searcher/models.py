from django.db import models


class QueryParam(models.Model):
    q = models.CharField(max_length=200, blank=True)
    accepted = models.BooleanField(blank=True)
    answers = models.IntegerField(null=True)
    body = models.CharField(max_length=200,  blank=True)
    closed = models.BooleanField(blank=True)
    migrated = models.BooleanField(blank=True)
    notice = models.BooleanField(blank=True)
    tagged = models.CharField(max_length=200,  blank=True)
    title = models.CharField(max_length=200,  blank=True)
    user = models.IntegerField(null=True)
    url = models.URLField(max_length=200, blank=True)
    views = models.IntegerField(null=True)
    wiki = models.BooleanField(blank=True)

    # TODO: another field must be mentioned if this is used
    nottagged = models.CharField(max_length=200,  blank=True)

    ORDER_CHOICES = [
        ("desc", "desc"),
        ("asc", "asc"),
    ]
    order = models.CharField(
        max_length=5,
        default="desc",
        choices=ORDER_CHOICES
    )

    SORT_CHOICES = [
        ("activity", "activity"),
        ("creation", "creation"),
        ("votes", "votes"),
        ("relevance", "relevance"),
    ]
    sort = models.CharField(
        max_length=10,
        default="activity",
        choices=SORT_CHOICES
    )
