from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=185, blank=False)  # longest Wikipedia article is 185 chars counting spaces
    article_html = models.TextField(blank=False)
    last_edited = models.DateTimeField(auto_now=True)
    last_edited_by = models.CharField(max_length=30, default='anonymous', blank=False)

    def __str__(self):
        return 'Article' + self.title

    def formatted_title(self):
        return self.title.replace('_', ' ')