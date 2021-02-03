from django.db import models

class category(models.Model):
    name   = models.CharField(max_length = 128, unique = True)

    def __str__(self):
        return self.name

class page(models.Model):
    category = models.ForeignKey(category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default = 0 )

    def __str__(self):
        return self.title

# Create your models here.
