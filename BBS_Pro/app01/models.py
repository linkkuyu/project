from django.db import models

# Create your models here.

class BBS(models.Model):
     title = models.CharField(max_length=64)



class Comment(models.Models):
    pass

class Category(models.Model):
    pass

class BBS_user(models.Model):
    pass



