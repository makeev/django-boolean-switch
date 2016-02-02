.. image:: https://badge.fury.io/py/django-boolean-switch.svg
    :target: http://badge.fury.io/py/django-boolean-switch

=====
django-boolean-switch
=====

Simple app to change your boolean fields in admin list view quickly in one click

Usage
-----------

1. Getting the code for the latest stable release use 'pip'::
    
    pip install django-boolean-switch

2. Add "boolean_switch" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'boolean_switch',
    )

3. Include the boolean_switch URLconf in your project urls.py like this::

    url(r'^admin/', include('boolean_switch.urls')),
    ...
    url(r'^admin/', include(admin.site.urls)),

4. Use mixin to modify you admin output::

    from boolean_switch.admin import AdminBooleanMixin

    class MyModelAdmin(AdminBooleanMixin, admin.ModelAdmin):
        list_display = ['sometitle', 'somebooleanfiled']

5. Now you can change boolean fields flag from list view in one click!

.. image:: http://s30.postimg.org/hqngbv1up/ezgif_com_resize.gif
