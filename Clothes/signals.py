from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Clothets

def user_register(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='viewer'))
        Clothets.objects.create(
            user = instance,
            nameC = instance.username,
        )
        print("Generated")

post_save.connect(user_register, sender=User)
