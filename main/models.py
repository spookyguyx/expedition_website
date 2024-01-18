from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    result_expedition = models.TextField()
    photo_home =models.ImageField()
    current_expedition = models.BooleanField()
    photo_archive = models.FileField()
    video = models.CharField(max_length=100)
    article_slug = models.SlugField()

    def __str__(self):
        return self.name




class Partners(models.Model):
    partners_id = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    partners = models.TextField()
    photo_partners = models.ImageField()


class ArticleImage(models.Model):
    post = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    images = models.FileField()

    def __str__(self):
        return self.images.name


class Map(models.Model):
    post = models.ForeignKey("Article", default=None, on_delete=models.CASCADE, null=True, blank=True)
    maps = models.CharField(max_length=100)


class Events(models.Model):
    event_id = models.ForeignKey("Article", on_delete=models.CASCADE)
    title_event = models.CharField(max_length=100)
    date_event = models.DateField()
    photo_events = models.ImageField()
    description_event = models.TextField()

    def __str__(self):
        return self.title_event


class Team(models.Model):
    team_id = models.ForeignKey("Article", on_delete=models.CASCADE)
    members_name = models.CharField(max_length=25)
    role_member = models.CharField(max_length=50)
    photo_members = models.FileField()


class Slider(models.Model):
    photo = models.ImageField()


class News(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()
    video = models.TextField()

    def __str__(self):
        return self.name


class Anons(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


