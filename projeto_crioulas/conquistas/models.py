from django.db import models


class Conquista(models.Model):
    ano = models.IntegerField(verbose_name="Ano")
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    # As fotos irão para a pasta media/conquistas/
    imagem = models.ImageField(upload_to='conquistas/', verbose_name="Imagem de Fundo")

    class Meta:
        ordering = ['ano'] # Ordena do mais antigo para o mais novo
        verbose_name = "Conquista"
        verbose_name_plural = "Conquistas"

    def __str__(self):
        return f"{self.ano} - {self.titulo}"