from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
STATUS = (("Closing","Closing"), ("Structuring","Structuring"),("Push", "Push"))
DEVISE = (("Eur","Eur"), ("Dollar","Dollar"),("Sol", "Sol"))

class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    montant = models.DecimalField(decimal_places=2, max_digits=900)
    devise = models.CharField(choices=DEVISE,default="Eur",max_length=20)
    zone = models.CharField(default="0",choices=STYLE_CHOICES, max_length=100)
    brower = models.CharField(default="0",max_length=100)
    lender = models.CharField(default="0",max_length=100)
    status = models.CharField(choices=STATUS, default="Waiting",max_length=20)

    class Meta:
        ordering = ['created']
