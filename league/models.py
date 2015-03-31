from django.db import models
from django.utils import timezone

# Create your models here.
class Player (models.Model):
    name = models.CharField(unique=False, max_length=50)
    playerid = models.CharField(unique = True, max_length=12)
    number = models.IntegerField(max_length=3, null=True)
    position = models.CharField(unique=False, max_length=50, null=True)
    games_played = models.IntegerField(max_length=3, null=True)
    goals = models.IntegerField(max_length=3, null=True)
    height = models.IntegerField(max_length=3, null=True)
    weight = models.IntegerField(max_length=3, null=True)


    class Meta(object):
        ordering = ('number', 'name')

    def __unicode__(self):
        return U'%s %s' %(self.name, self.id) 

class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    mascot = models.CharField(unique=False, max_length=50, null=True)
    coach = models.CharField(max_length=50)
    description = models.CharField(max_length = 200, default='')
    players = models.ManyToManyField('Player')

    class Meta(object):
        verbose_name_plural = 'Teams'
        ordering = ('name', 'mascot')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.mascot)
          

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Team, self).save(*args, **kwargs)
