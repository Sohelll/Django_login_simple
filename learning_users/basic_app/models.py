from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #the User class already has fname, lname, email, password etc, we define additional elements AuthenticationMiddleware

    # additional classses

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

    #username is the default attribute
