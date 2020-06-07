from django.db import models


class Session(models.Model):
    id_session = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=300, blank=False,
        null=False
    )
    order = models.IntegerField(
        blank=False, null=False
    )
    translate_key = models.CharField(
        max_length=300, blank=True,
        null=True
    )
    status = models.BooleanField(
        default=False
    )
    description = models.TextField(
        blank=True,null=True
    )
    cover = models.ImageField(
        blank=True, null=True
    )
    router = models.CharField(
        max_length=100, blank=True,
        null=True
    )
    code = models.CharField(
        max_length=10, blank=True,
        null=True
    )

    def __str__(self):
        return self.name
