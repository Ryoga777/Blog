from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(upload_to='media/', default='no-image.jpg')
    content = models.TextField()
    date = models.DateTimeField(auto_now = False, auto_now_add = True)
    slug = models.SlugField(max_length = 120)
    author = models.ForeignKey(User, on_delete= models.CASCADE, default = 1)

    def get_absolute_url(self):
        return reverse("singolo", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.title