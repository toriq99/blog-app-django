from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100, default='FIRST NAME')
    last_name = models.CharField(max_length=100, default='LAST NAME')
    email = models.EmailField(default='SOME STRING')

    def __str__(self):
        return f"{self.first_name}"

class Post(models.Model):
    title = models.CharField(max_length=150, null=True)
    excerpt = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)], null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}, {self.author}"

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)