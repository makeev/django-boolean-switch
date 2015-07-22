.. image:: https://badge.fury.io/py/django-boolean-switch.svg
    :target: http://badge.fury.io/py/django-boolean-switch

=====
django-boolean-switch
=====

Simple app to change your boolean fields in admin list view quickly in one click

Usage
-----------

1. Add "boolean_switch" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'boolean_switch',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^admin/', include('boolean_switch.urls')),

3. Use mixin to modify you admin output::

    class MyModelAdmin(AdminBooleanMixin, admin.ModelAdmin):
        list_display = ['sometitle', 'somebooleanfiled']

4. Now you can change boolean fields flag from list view in one click!

