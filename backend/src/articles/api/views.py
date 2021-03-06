from rest_framework import viewsets

from articles.models import Articles
from .serializers import ArticleSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
  queryset = Articles.objects.all()
  serializer_class = ArticleSerializer

# class ArticlesListView(ListAPIView):
#   queryset = Articles.objects.all()
#   serializer_class = ArticleSerializer

# class ArticlesCreateView(CreateAPIView):
#   queryset = Articles.objects.all()
#   serializer_class = ArticleSerializer

# class ArticlesDetialView(RetrieveAPIView):
#   queryset = Articles.objects.all()
#   serializer_class = ArticleSerializer

# class ArticlesUpdateView(UpdateAPIView):
#   queryset = Articles.objects.all()
#   serializer_class = ArticleSerializer

# class ArticlesDestroyView(DestroyAPIView):
#   queryset = Articles.objects.all()
#   serializer_class = ArticleSerializer
