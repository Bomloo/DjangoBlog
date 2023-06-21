from django.db import models

# Create your models here.
# inherites Model from models
class Article(models.Model):
    # python manage.py makemigrations will create file to migrate to database
    # python manage.py migrate will migrate model format over
    # any changes to models will need to remigrate with above steps

    # use orm to interact with database through django models
    # from articles.models (models file in articles folder) import Article (class)
    # Article.objects.all() (check all Article objects)
    # name = Article() (new Article object instance)
    # name.title = title (assigning title to Article object instance)
    # name.save() (save object instance to table)
    # Article.objects.all() (will show new model by title name)

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
    # thumbnail for articles, we will use a default if there is none
    thumb = models.ImageField(default = "default.png", blank = True)
    # add author later

    # when Article object instance is called, represented in string format
    # in this case, it is self.title
    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:50] + "..."
