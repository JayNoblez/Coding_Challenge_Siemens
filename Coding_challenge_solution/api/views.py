from django.shortcuts import render
from rest_framework import viewsets
from .models import Topic, Article
from .serializers import TopicSerializer, ArticleSerializer
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
class TopicView(viewsets.ModelViewSet):
  queryset = Topic.objects.all()
  serializer_class = TopicSerializer

class ArticleView(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

class TopicFetchView(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

  def get_queryset(self):
    """
    This view should return a list of all the purchases for
    the user as determined by the username portion of the URL.
    """
    print(f"Topic Name: {self.kwargs['topic']}")
    qs = super().get_queryset()
    return qs.filter(topic__name=self.kwargs['topic'])


class TopicAddView(viewsets.ModelViewSet):
  queryset = Topic.objects.all()
  serializer_class = TopicSerializer

  def create(self, topic):
    Topic.objects.get_or_create(name=topic)


  def get_queryset(self, **kwargs):
    """
    This view should return a list of all the purchases for
    the user as determined by the username portion of the URL.
    """
    self.create(self.kwargs['topic'])

    qs = super().get_queryset()
    return qs.filter(name=self.kwargs['topic'])


class TopicUpdateView(viewsets.ModelViewSet):

  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

  def get_queryset(self):
    """
    This view should return a list of all the purchases for
    the user as determined by the username portion of the URL.
    """
    print(f"Topic Name: {self.kwargs['topic']}")
    qs = super().get_queryset()
    return qs.filter(topic__name=self.kwargs['topic'])

  def post(self, request, topic):
    print(request.POST)
    try:
      t = Topic.objects.get(name=topic)
      a = Article(topic=t, article=request.POST['article'])
      a.save()
    except:
      return HttpResponse('{ "result" : "failure", "error" : "Topic does not exist" }')
    return HttpResponseRedirect(f'{topic}')
