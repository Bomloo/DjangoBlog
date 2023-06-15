from django.db import models

# Create your models here.
# inherites Model from models
class Article(models.Model):
    # field type for each data column
    # text field = large amount of text
    # char field = little amount of text

    # title will be a column of charfield (little text)
    # titles cannot by more than 100
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    # will give date that article is created, automaticly dates at time of
    # creation
    date = models.DateTimeField(auto_now_add = True)
    # add in thumbnail later
    # add author later
