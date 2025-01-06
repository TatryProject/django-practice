from rest_framework import serializers

from imdb.models import TitleBasic

class TitleBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = TitleBasic
    fields = [
      't_const',
      'title_type',
      'primary_title',
      'original_title',
      'is_adult',
      'start_year',
      'end_year',
      'runtime_minutes',
      'genres'
    ]