from django.contrib.auth.models import User
from django.db import models

# Create your models here.


"""class ProfilePicture(models.Model):
    image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image"""


#class SearchHistory(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #search_history = models.ForeignKey(SearchHistory, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=9999, null=True)
    def __str__(self):
        return self.profile_pic
