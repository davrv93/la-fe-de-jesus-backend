from django.db import models
from session.models.session import Session
from model_clone import CloneMixin


class Section(CloneMixin, models.Model):
    id_section = models.AutoField(primary_key=True)
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
    cover = models.ImageField(
        blank=True, null=True
    )
    code = models.CharField(
        max_length=100, blank=True,
        null=True
    )
    session = models.ForeignKey(
        Session,
        db_column='id_session',
        on_delete=models.PROTECT,
        related_name='section_session_set',
        blank=False, null=False
    )
    type = models.CharField(
        choices=(
            ('P', 'Preguntas'),
            ('Q', '¿Qué debo hacer?'),
            ('R', 'Mi resolución'),
            ('DC', 'Datos de contacto'),
            ('DP', 'Datos personales'),
            ('S', 'Saludo'),
            ('D', 'Despedida'),
        ),
        max_length=2,
        blank=True,null=True
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return str(self.session.name) + ': ' + str(self.name)
