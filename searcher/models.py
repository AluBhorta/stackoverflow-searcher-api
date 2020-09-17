from django.db import models


class QueryHash(models.Model):
    query_param_hash = models.IntegerField(primary_key=True)
    question_ids = models.CharField(max_length=500, blank=True)
    has_more = models.BooleanField(blank=True)


class ShallowUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    reputation = models.IntegerField(null=True)
    display_name = models.CharField(max_length=200, blank=True)
    profile_image = models.URLField(max_length=200, blank=True)
    link = models.URLField(max_length=200, blank=True)

    USER_TYPE_CHOICES = [
        ("unregistered", "unregistered"),
        ("registered", "registered"),
        ("moderator", "moderator"),
        ("team_admin", "team_admin"),
        ("does_not_exist", "does_not_exist")
    ]
    user_type = models.CharField(
        max_length=20,
        default="registered",
        choices=USER_TYPE_CHOICES,
        blank=True
    )


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    is_answered = models.BooleanField(blank=True)
    view_count = models.IntegerField(null=True)
    answer_count = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    last_activity_date = models.IntegerField(null=True)
    creation_date = models.IntegerField(null=True)

    content_license = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(
        ShallowUser,
        on_delete=models.CASCADE,
        to_field="user_id",
        blank=True
    )
