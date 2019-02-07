from django.db import models

# Create your models here.
class Topic(models.Model):
  name = models.CharField(max_length=50, unique=True, blank=False)
  articles_count = lambda self: self.article_set.count()

class Article(models.Model):
  topic = models.ForeignKey(
            'Topic',
            on_delete=models.CASCADE,
          )
  article = models.CharField(max_length=512)

  def __unicode__(self):
      return self.article

  @property
  def topic_name(self):
      return self.topic.name


