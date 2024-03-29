from distutils.version import StrictVersion

from django import get_version
from django.forms import widgets
from django.db.models import BooleanField
from django.utils.html import mark_safe
try:
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ImportError:
    from django.templatetags.static import static


try:
    # Django 1.8
    from django.core.exceptions import FieldDoesNotExist
except ImportError:
    # Django 1.7
    from django.db.models.fields import FieldDoesNotExist

img_extension = 'gif'
if StrictVersion(get_version()) > '1.9':
    img_extension = 'svg'


def boolean_switch_field(field):
    def _f(self):
        v = getattr(self, field.name)
        url = '%d/%s/switch/' % (self._get_pk_val(), field.name)
        img_path = static('admin/img/icon-%s.%s' % (('no','yes')[v], img_extension))
        return mark_safe('<a href ="%s" class="boolean_switch"><img src="%s" alt="%d" /></a>' % (
            url, img_path, v
        ))
    _f.short_description = field.verbose_name
    _f.admin_order_field = field.name
    _f.allow_tags = True
    return _f


class AdminBooleanMixin(object):
    """
    Change boolean fields presence in list
    """

    @property
    def media(self):
        m = super(AdminBooleanMixin, self).media
        return m + widgets.Media(js=('boolean_switch/boolean_switch.js',))

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        list_display = []
        for field_name in self.list_display:
            try:
                db_field = self.model._meta.get_field(field_name)
                if isinstance(db_field, BooleanField):
                    field_name = boolean_switch_field(db_field)
            except FieldDoesNotExist:
                pass
            list_display.append(field_name)
        return list_display
