from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=100)
    statement = models.TextField()
    source = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Solution(models.Model):
    title = models.CharField(max_length=100)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    algorythm = models.TextField()
    code = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title