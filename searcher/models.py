from django.db import models


class QueryParam(models.Model):
    q = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200,  blank=True)
    body = models.CharField(max_length=200,  blank=True)
    tagged = models.CharField(max_length=200,  blank=True)
    # TODO: another field must be mentioned if nottagged is used
    nottagged = models.CharField(max_length=200,  blank=True)

    accepted = models.BooleanField(blank=True)
    closed = models.BooleanField(blank=True)
    migrated = models.BooleanField(blank=True)
    notice = models.BooleanField(blank=True)
    wiki = models.BooleanField(blank=True)

    answers = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    views = models.IntegerField(null=True)

    url = models.URLField(max_length=200, blank=True)

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

    # TODO: add
    # page
    # pagesize
    #
    # min
    # max
    # fromdate
    # todate


class ShallowUser(models.Model):
    user_id = models.IntegerField(null=False, primary_key=True)
    reputation = models.IntegerField(null=False)
    display_name = models.CharField(max_length=200,  blank=False)
    profile_image = models.URLField(max_length=200, blank=False)
    link = models.URLField(max_length=200, blank=False)

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
        choices=USER_TYPE_CHOICES
    )


class Question(models.Model):
    question_id = models.IntegerField(null=False, primary_key=True)
    is_answered = models.BooleanField(blank=False)
    view_count = models.IntegerField(null=False)
    answer_count = models.IntegerField(null=False)
    score = models.IntegerField(null=False)
    last_activity_date = models.IntegerField(null=False)
    creation_date = models.IntegerField(null=False)
    content_license = models.CharField(max_length=200,  blank=False)
    title = models.CharField(max_length=200,  blank=False)
    link = models.URLField(max_length=200, blank=False)

    tags = models.CharField(max_length=200,  blank=True)
    owner = models.ForeignKey(
        ShallowUser,
        on_delete=models.CASCADE,
        to_field="user_id"
    )


# class SearchResult(models.Model):
#     questions = models.ManyToManyField(to=Question)
#     # qp = models.OneToOneField
