""" This module contains the models """

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class FilePathModel(models.Model):
    """ models of file path """

    title = models.CharField(_('Título'), max_length=200)
    slug = models.SlugField(unique=True, max_length=200)

    path_root = models.CharField(_('Pasta raiz'), max_length=255)
    path_url = models.CharField(_('URL raiz'), max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:200]

        super(FilePathModel, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        """ return url to file path """
        return 'core:file_serve', (self.slug, self.path_root)

    def __str__(self):
        return "%s - %s" % (self.title, self.path_root)

    class Meta:
        """ meta data of model """
        verbose_name = _('Pasta de arquivo')
        verbose_name_plural = _('Pasta de arquivos')


class LinksModel(models.Model):
    """ models of inks """

    title = models.CharField(_('Título'), max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    link_url = models.CharField(_('URL raiz'), max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:200]

        super(LinksModel, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        """ return url to redirect link """
        return 'core:redirect_link', (self.slug)

    def __str__(self):
        return "%s - %s" % (self.title, self.link_url)

    class Meta:
        """ meta data of model """
        verbose_name = _('Link')
        verbose_name_plural = _('links')
