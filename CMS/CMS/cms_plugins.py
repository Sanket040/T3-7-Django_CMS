from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from .models import Music
@plugin_pool.register_plugin
class MusicPlugin(CMSPluginBase):
    model = Music
    render_template = "music_plugin.html"
    cache = False