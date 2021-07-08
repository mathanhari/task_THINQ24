from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete")
)
class posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    content = models.TextField()
    metades = models.CharField(max_length=300, default="new post")
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.FileField(upload_to='img')
    class Meta:
        ordering = ['-created_on']

    # used while managing models from terminal
    def __str__(self):
        return self.title
#
# class Comment(models.Model):
#     post = models.ForeignKey(posts, on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     # created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
# #
#     def approve(self):
#         self.approved_comment = True
#         self.save()
# #
#     def __str__(self):
#         return self.text