from django.db import models


class Avatar(models.Model):
    hair_color = models.CharField(max_length=50, default="Black")
    skin_tone = models.CharField(max_length=50, default="Light")
    accessories = models.JSONField(default=list)  # Store accessories as a list

    def __str__(self):
        return f"Avatar ({self.hair_color}, {self.skin_tone})"


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BehaviorLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)  # 
