from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True, max_length=70)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    info = models.TextField('Write something about your self', blank=True, max_length = 375)

    def __str__(self):
        return f'{self.user.username.capitalize()} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
