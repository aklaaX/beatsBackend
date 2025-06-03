from django.db import models

# Create your models here.
class Beat(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Core.User', on_delete=models.CASCADE, related_name='beats')
    duration = models.CharField(max_length=10)  # e.g., '3:45'
    audio = models.FileField(upload_to='beats/audio/')
    coverImage = models.ImageField(upload_to='beats/covers/', blank=True, null=True)
    isPublished = models.BooleanField(default=False)
    genre = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Beats'