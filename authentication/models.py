from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """
    Забезпечує повну реалізацію користувача,
    за замовчуванням як абстрактної моделі.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = models.CharField(
        primary_key=False, max_length=150,
        verbose_name="Користувач"
    )

    email = models.EmailField(
        max_length=100, unique=True,
        verbose_name="Електронна пошта"
    )
    avatar = models.ImageField(upload_to='uploads/avatar/%Y/%m/%d/',
                               default='uploads/avatar/default.png',
                               blank=True,
                               verbose_name="Аватарка")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
