import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    id = models.UUIDField(_('UUID'), primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(_('Creation Time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        abstract = True
