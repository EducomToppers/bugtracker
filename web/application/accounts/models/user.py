from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # create Fk to globalUserProfileId here

    def __str__(self):
        return self.username
