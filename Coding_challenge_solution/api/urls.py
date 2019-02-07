from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/topics', views.TopicView)
# router.register('api/article', views.ArticleView)

urlpatterns = [
  path('', include(router.urls)),

  # Url to fetch topic & article info
  path( 'api/topics',
        views.TopicView.as_view({'get': 'list'})),

  # Url to fetch topic & article info
  path( 'api/fetch/<topic>',
        views.TopicFetchView.as_view({'get': 'list'}),
        name='topic'),

  # Url to add a new topic
  path( 'api/add/<topic>',
        views.TopicAddView.as_view({'get': 'list'}),
        name='topic'),
  
  # Url to add a new article under a topic
  path( 'api/update/<topic>',
        views.TopicUpdateView.as_view({'get': 'list'}),
        name='topic'),
]
