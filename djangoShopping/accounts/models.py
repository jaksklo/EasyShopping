from django.db import models
from django.contrib import auth
# Create your models here.
from django.urls import reverse_lazy, reverse


class ESUser(auth.models.User, auth.models.PermissionsMixin):

    SEXES = [('M','male'),('F','female'),('O','other')]

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'profiles/user_{0}/{1}'.format(instance.pk,filename)

    origin = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(choices=SEXES, max_length=1)

    # profile_pic = models.ImageField(upload_to=user_directory_path, default='profiles/default_pic.png',blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path, blank=False)

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse('accounts:userdetails', kwargs={'pk': self.pk})
