from django.db import models

class TodoItemList(models.Model):
    content = models.TextField()
