from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class TitleBasic(models.Model):
  t_const = models.TextField(primary_key=True, db_column="tconst")
  title_type = models.TextField(db_column="titleType")
  primary_title = models.TextField(db_column="primaryTitle")
  original_title = models.TextField(db_column="originalTitle")
  is_adult = models.BooleanField(db_column="isAdult")
  start_year = models.IntegerField(db_column="startYear")
  end_year = models.IntegerField(db_column="endYear", null=True)
  runtime_minutes = models.IntegerField(db_column="runtimeMinutes")
  genres = ArrayField(base_field=models.TextField())

  class Meta:
    db_table = "title_basics"
