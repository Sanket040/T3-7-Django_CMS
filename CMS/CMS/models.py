from cms.models.pluginmodel import CMSPlugin
from django.db import models
from tinymce.models import HTMLField
class Music(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')
    body = HTMLField()