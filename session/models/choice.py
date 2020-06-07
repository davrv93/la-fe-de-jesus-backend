from django.db import models
from session.models.item import Item


class Choice(models.Model):
    id_choice = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=300, blank=False,
        null=False
    )
    order = models.IntegerField(
        blank=False, null=False
    )
    content = models.CharField(
        max_length=300, blank=True,
        null=True
    )
    isCorrect = models.BooleanField(
        default=True
    )
    status = models.BooleanField(
        default=True
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
    item = models.ForeignKey(
        Item,
        db_column='id_item',
        related_name='choice_item_set',
        on_delete=models.PROTECT,
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

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return (str(self.item.section.session.name) + ': ' + str(
            self.item.section.name) + ' ' + self.item.name + '-' + self.name)
