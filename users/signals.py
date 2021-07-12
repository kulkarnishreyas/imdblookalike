# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import Profile
# from django.dispatch import receiver

# # receiver decoration will identify which event is being handled.
# # post_save means that the signal is triggered after the model is saved in db (User created/updated)
# # created boolean to see if the object was indeed created.
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
    

# # save profile when profile is edited.
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
