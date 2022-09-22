from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Guitars(models.Model):
    """
    Guitars Model
    """
    guitar_model = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guitars')
    description = models.TextField()
    guitar_image = CloudinaryField('image', null=False, blank=False)
    remaining_guitars = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='guitar_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.guitar_model

    def number_of_likes(self):
        return self.likes.count()