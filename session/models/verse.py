from django.db import models


class Verse(models.Model):
    id_verse = models.AutoField(primary_key=True)
    chapter = models.IntegerField(
        blank=False, null=False
    )
    verse = models.IntegerField(
        blank=False, null=False
    )
    book = models.CharField(
        max_length=300, blank=True,
        null=True
    )
    translate_key = models.CharField(
        max_length=300, blank=True,
        null=True
    )
    status = models.BooleanField(
        default=True
    )
    content = models.TextField(
        blank=True,null=True
    )


    class Meta:
        ordering = ('chapter','verse')

    def __str__(self):
        return str(self.book) + ' ' + str(self.chapter) +':' + str(self.verse)
