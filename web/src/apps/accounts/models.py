from django.contrib.auth.models import AbstractUser
from model_utils import Choices
from django.db import models


class User(AbstractUser):
    PURPOSE = Choices(
        (0, "blogger", "Blogger"),
        (1, "creator", "Creator"),
        (2, "subscriber", "Subscriber"),
        (3, "the_others", "The_others"),
    )
    username = models.CharField(
        max_length=150, db_column="username", verbose_name="username", unique=True
    )
    email = models.EmailField(db_column="email", verbose_name="email", unique=True)
    purpose = models.IntegerField(
        db_column="purpose",
        verbose_name="purpose",
        choices=PURPOSE,
        default=PURPOSE.the_others,
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자 리스트"
        ordering = ("username",)
