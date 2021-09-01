from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone


# Create your models here.

class Brands(models.Model):
    Brd = [
        ('N','Nike'),
        ('As','Asics'),
        ('Ad','Adidas'),
        ('Sa','Salomon'),
        ('Ho','HokaOneOne')
    ]
    nameB = models.CharField(max_length=10,choices=Brd,default='N')

    def __str__(self):
        return self.nameB

class Targets(models.Model):
    Tar = [
        ('Esy', 'Easy'),
        ('Tmp', 'Tempo'),
        ('Lng', 'Long')
    ]
    nameT = models.CharField(max_length=10,choices=Tar,default='Esy')


    def __str__(self):
        return self.nameT

class Shoes(models.Model):
    Sur = [
        ('Trl','Trail'),
        ('Rd','Road')
    ]
    nameS = models.CharField(max_length=20)
    surface = models.CharField(max_length=10,choices=Sur,default='Rd')
    milage = models.FloatField(max_length=10)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    target = models.ManyToManyField(Targets)


    def __str__(self):
        return self.nameS


class Clothets(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile1.png",null=True,blank=True)
    nameC = models.CharField(max_length=10)
    shoe = models.ManyToManyField(Shoes)

    def __str__(self):
        return self.nameC

class Runs(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # DateTimeField(default=timezone.now)
    target = models.ForeignKey(Targets, on_delete=models.CASCADE)
    mileage = models.FloatField(max_length=3)
    duration = models.DateTimeField(blank=True)
    pace = models.IntegerField(max_length=3)
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    runner = models.ForeignKey(Clothets, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d")
    







