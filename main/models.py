from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class Article(models.Model):
    name = models.CharField(max_length=50, blank=True)
    name_long = models.CharField(max_length=75, blank=True)
    text = models.TextField(blank=True)
    current_expedition = models.BooleanField(blank=True)
    video = models.CharField(max_length=100, blank=True)
    article_slug = AutoSlugField(populate_from='name', editable=True, always_update=True, blank=True)

    def get_absolute_url(self):
        return f'/admin/admin_exp'


class PhotoHome(models.Model):
    photo_home_id = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    photo_home = models.ImageField()


class ResultsExpedition(models.Model):
    result = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    text_result = models.TextField()
    image = models.ImageField()


class Partners(models.Model):
    partners_id = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    partners = models.TextField()
    photo_partners = models.ImageField()


class ArticleImage(models.Model):
    post = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField()

    def __str__(self):
        return self.images.name


class Map(models.Model):
    post = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    maps = models.CharField(max_length=100)


class Events(models.Model):
    event_id = models.ForeignKey("Article", on_delete=models.CASCADE)
    title_event = models.CharField(max_length=100)
    date_event = models.CharField(max_length=25)
    photo_events = models.ImageField()
    description_event = models.TextField()
    slug = AutoSlugField(populate_from='title_event', editable=True, always_update=True, blank=True)

    def __str__(self):
        return self.title_event


class Team(models.Model):
    team_id = models.ForeignKey("Article", on_delete=models.CASCADE)
    members_name = models.CharField(max_length=75)
    role_member = models.CharField(max_length=50)
    photo_members = models.ImageField(blank=True)


class Slider(models.Model):
    photo = models.ImageField()


class News(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()
    video = models.TextField()
    news_slug = AutoSlugField(populate_from='name', editable=True, always_update=True, blank=True)

    def __str__(self):
        return self.name


class Anons(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


