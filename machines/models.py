from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Machine(models.Model):
    hostname = models.CharField(max_length=200)

    ARCHS = (
        ('sparc', 'sparc platform'),
        ('i386', 'x86 platform'),
    )
    arch = models.CharField(max_length=5, choices=ARCHS)

    location = models.CharField(max_length=10)

    STATUS = (
        ('A', 'available'),
        ('R', 'reserved'),
    )
    status = models.CharField(max_length=1, choices=STATUS)
    user = models.ForeignKey(User)
    note = models.TextField()

    def __str__(self):
        return self.hostname    


@python_2_unicode_compatible
class OS(models.Model):
   pass 
