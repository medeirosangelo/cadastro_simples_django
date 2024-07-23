from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name = "Título", max_length=100, null=False, blank=False
    )  # O título não pode ser nulo ou em blanco
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)  # aquele horario específico que ele foi criado
    deadline = models.DateField(verbose_name="Data de Entraga", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
