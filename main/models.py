from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#######USERS############
class UserPerfil(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    foto = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Materiais(models.Model):

    tipo=models.CharField(max_length=8)
    #(pdf,slide,video)
    titulo=models.CharField(max_length=256)
    desc=models.CharField(max_length=512)
    link=models.URLField()
    upvotes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)
    pertencea=models.ForeignKey('Licao',on_delete=models.CASCADE)


class Curriculo(models.Model):

    titulo=models.CharField(max_length=256)
    desc=models.CharField(max_length=512)
    autor=models.ForeignKey('UserPerfil',on_delete=models.CASCADE)

    upvotes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)


class Licao(models.Model):

    titulo=models.CharField(max_length=256)
    desc=models.CharField(max_length=512)
    upvotes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)
    pertencea=models.ForeignKey('Curriculo',on_delete=models.CASCADE)