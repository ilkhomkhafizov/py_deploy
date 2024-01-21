from django.db import models


class Category(models.Model):
    name = models.CharField("Catrgory name", max_length=100)

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    age = models.SmallIntegerField(null=True)
    father_age = models.SmallIntegerField(null=True)

    def __str__(self) -> str:
        return self.title
