from cloudinary.models import CloudinaryField
from django.db import models
from django.conf import settings


class Twet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    twet = models.ForeignKey(Twet, related_name="likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "twet")  # prevents duplicate likes

    def __str__(self):
        return f"{self.user.username} liked {self.twet.id}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    twet = models.ForeignKey(Twet, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"