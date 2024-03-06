from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from utils.models import AbstractModel


class CustomUser(AbstractModel, AbstractUser):
    phone = models.CharField(_('Phone Number'),max_length=20, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
