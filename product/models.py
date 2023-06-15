from django.db import models

from django.core.files import File
from io import BytesIO
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPcAAADMCAMAAACY78UPAAAAMFBMVEW8vsDn6Onq6+y5u73CxMbIycvh4uPW2NnR09Tc3d/AwsTk5ebU1dfg4eK9v8HOz9HoolfoAAADEUlEQVR4nO3c63KqMBRAYZINVUTw/d/2yNVEg4JHkZ2s709nOuKwhhSDhGYZAAAAAAAAAAAAAAAAACROpCkKkV/vxtbkUtmrukirvKmt6dhzSuHyZ0YphcvZmlt48evd2YwY1yGZA15YLzyZ7qPXbfNf789W7rpPv96fraQ6zptEz2upfo5lUiU3b+krk5unytA5XJeUw3XJ6Rh3vpT2MoRLVhTD0c+kHn8dp2v29Tz2UNid5/J4w9ts8xjen95ttOF99sMnlxyGX0caPmXfT1Skjjl8OqyP87OYw+Uym92Gm0jDp+zwPGX8JiK28BfZt0uVuMLl+CLbDd9yx77rmt17NhlvTP8aE1F4M/xcMoab5vVrAGArxTft9zwvlf2i/X7v6tzm/AK694Zuuummm+74uj81W1HWfc4/pFbVbT91n09KuuneGbrvu6Xzzluq7m7OdVWZwxv3BDR3S2GG2wbrFzVo7s6nycf6cM3d5mb1XSDF3Rd3Vebandfb7ex5K53uys0OLz6eL4ql2wTv+s3fJ1Xc7Y3zKrTKo5xfm6u32zuvhb78b9dCVLNvqbfbG+iBYX6yM6t9uo31dr+Yt/QbzY10zd2SV125NaHscQ1+uEpzd/snXBpbHkPbjINh5spVd/dwIRraZPrjD09htXfPbeF8yIU+4qLqdk717hNVwVVeEXVLNY3o5uWDgxF1/01L86Q2nsBIj6a7X47dhYv/vGRwpMfSPa5Cb8Pzu+zQSI+kW6bJen73FPjMSI+j2zl/V+ORfz7S4+h2R7Z/WT430qPoPgVTfX93Nxxi6F6Q/TCz19+9cDWE/w2c/u7Fi0C8ka6+O3j6Dh9w79pdeffybH+kK++WYnm2N9J1d6/LnvkWWmH3kg9uL3wa6aq712Y7I11zt4SnpE8P+Li94u63Vm+O83S93VK+tT6zlmFrrd3jYqa1hm0Vd//XW9JN997QnWq3+Vi3rnX3yT5n8QV07w3ddNNNN92RdCf6fy2yTz0UGpTMv80GAAAAAAAAAAAAAAAAAAAAAAAAAAAAkKZ/TikowOqV20oAAAAASUVORK5CYII='

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail