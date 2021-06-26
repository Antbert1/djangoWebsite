from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ImageField(
    upload_to = 'img',
    default="null")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.author
