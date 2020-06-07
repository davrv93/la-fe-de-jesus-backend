from django.db import models
from session.models.section import Section
from session.models.verse import Verse
from model_clone import CloneMixin




class Item(CloneMixin,models.Model):
    id_item = models.AutoField(primary_key=True,
                               db_column='id_item')

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
        default=True
    )
    description = models.TextField(
        blank=True,null=True
    )
    help = models.TextField(
        blank=True,null=True
    )
    cover = models.ImageField(
        blank=True, null=True
    )
    code = models.CharField(
        max_length=100, blank=True,
        null=True
    )
    section = models.ForeignKey(
        Section,
        db_column='id_section',
        on_delete=models.PROTECT,
        related_name='item_section_set',
        blank=False, null=False
    )
    type = models.CharField(
        choices=(
            ('P', 'Pregunta'),
            ('T', 'Texto'),
            ('H', 'HTML'),
            ('PA', 'Pregunta Abierta'),
            ('PC', 'Pregunta cerrada'),
            ('PM', 'Pregunta múltiple'),
            ('PU', 'Pregunta única'),
        ),
        max_length=2,
        blank=True,null=True
    )
    verse = models.ManyToManyField(
        Verse,related_name='item_verse_set', blank=True
    )

    _clone_many_to_many_fields = ['tags']

    class Meta:
        ordering = ('section__order', 'order')

    def __str__(self):
        return str(self.section.session.name) + ': ' + str(self.section.name) + ' ' + self.name
