from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('Адрес электронной почты', max_length=100,
                              unique=True)
    username = models.CharField('Уникальный юзернейм', max_length=50,
                                unique=True)
    password = models.CharField('Пароль', max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Пользователь'
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_user'
            )
        ]

    def __str__(self):
        return self.username
