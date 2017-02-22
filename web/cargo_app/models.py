from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class TxtFile(models.Model):
    qqfile = models.FileField(upload_to='cargo_app/')
    qqfilesolved = models.FileField(upload_to='cargo_app/', null=True)
    qquserid = models.CharField(max_length=255, null=True)
    qquuid = models.CharField(max_length=255)
    qqfilename = models.CharField(max_length=255, null=True)
    qqpartindex = models.IntegerField(null=True)
    qqchunksize = models.IntegerField(null=True)
    qqpartbyteoffset = models.IntegerField(null=True)
    qqtotalfilesize = models.IntegerField(null=True)
    qqtotalparts = models.IntegerField(null=True)
    qqworkdays = models.IntegerField(null=True)
    qqtotalweight = models.IntegerField(null=True)

    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TxtFile, self).save(*args, **kwargs)
