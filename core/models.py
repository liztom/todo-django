from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    todolist = models.ForeignKey(List)

    def __unicode__(self):
        return self.name