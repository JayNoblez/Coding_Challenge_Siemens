from rest_framework import serializers
from .models import Topic, Article

class TopicSerializer(serializers.ModelSerializer):

  class Meta:
    model = Topic
    fields = ('id', 'name', 'articles_count')


class ArticleSerializer(serializers.ModelSerializer):
  topic_name = serializers.ReadOnlyField()

  class Meta:
    model = Article
    fields = ('topic_name', 'article')