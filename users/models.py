from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
#cascase : if user is deleted, it will also delete the profile
# but if we delete the profile then it wont delete the user
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def sav(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height > 300 or img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.sav(self.image.path)