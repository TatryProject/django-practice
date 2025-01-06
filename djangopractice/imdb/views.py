from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Value


from imdb.models import TitleBasic
from imdb.serializers import TitleBasicSerializer

class ListPagination(PageNumberPagination):
  page_size = 25
  page_size_query_param = "page-size"
  max_page_size = 100
  page_query_param = "page"

@api_view(['GET'])
def detail(_, tconst):
  title_basic = get_object_or_404(TitleBasic, pk=tconst)
  return Response(TitleBasicSerializer(title_basic).data)

@api_view(['GET'])
def get_titles(request):
  title = request.query_params.get('title')
  year = request.query_params.get('year')
  genre = request.query_params.get('genre')
  
  queryset = TitleBasic.objects.all()
  if title is not None:
    queryset = queryset.filter(primary_title__icontains=title)
  if year is not None:
    queryset = queryset.filter(start_year__exact=year)
  if genre is not None:
    queryset = queryset.filter(genres__icontains=Value([genre]))

  paginator = ListPagination()
  paginated_queryset = paginator.paginate_queryset(queryset, request)
  serialized = TitleBasicSerializer(paginated_queryset, many=True)
  
  return paginator.get_paginated_response(serialized.data)
