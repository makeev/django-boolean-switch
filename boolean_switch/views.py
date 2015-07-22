# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils.translation import ugettext as _


def switch(request, url):
    """
    Set/clear boolean field value for model object
    """
    app_label, model_name, object_id, field = url.split('/')
    model = get_model(app_label, model_name)

    object = get_object_or_404(model, pk=object_id)
    if not request.user.has_perm('%s.change_%s' % (app_label, model.__name__), object):
        raise PermissionDenied

    setattr(object, field, getattr(object, field) == 0)
    object.save()

    if request.is_ajax():
        return JsonResponse({'object_id': object.pk, 'field': field, 'value': getattr(object, field)})
    else:
        msg = _(u'флаг %(field)s был изменен для %(object)s') % {'field': field, 'object': object}
        messages.success(request, msg)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
