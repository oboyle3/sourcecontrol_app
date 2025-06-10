from django.db import models
from django.contrib.auth.models import User

class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.repository.name} - {self.name}"

class Commit(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch.name}: {self.message[:50]}"
