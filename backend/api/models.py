import qrcode
from django.db import models
from io import BytesIO
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver

class Aluno(models.Model):

    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    foto = models.ImageField(upload_to="foto-aluno")

    qrcode = models.ImageField(upload_to="qrcode", blank=True, null=True, editable=False)
    
    def __str__(self):
        return self.nome


@receiver(post_save, sender=Aluno)
def criar_qrcode(sender, instance, created, **kwargs):
    if created:
        
        url = f"http://localhost:8000/aluno/{instance.id}"  

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        filename = f'aluno_{instance.id}_qrcode.png'

        instance.qrcode.save(filename, File(buffer), save=True)
