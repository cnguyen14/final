from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    customer_permissions = permission_class.objects.filter(content_type__app_label='store',
                                                           content_type__model='customer')

    order_permissions = permission_class.objects.filter(content_type__app_label='store',
                                                        content_type__model='order')

    orderitem_permissions = permission_class.objects.filter(content_type__app_label='store',
                                                            content_type__model='orderitem')

    shippingaddress_permissions = permission_class.objects.filter(content_type__app_label='store',
                                                                  content_type__model='shippingaddress')

    perm_view_customer = permission_class.objects.filter(content_type__app_label='store',
                                                         content_type__model='customer',
                                                         codename='view_customer')

    perm_view_order = permission_class.objects.filter(content_type__app_label='store',
                                                      content_type__model='order',
                                                      codename='view_order')

    perm_view_orderitem = permission_class.objects.filter(content_type__app_label='store',
                                                          content_type__model='orderitem',
                                                          codename='view_orderitem')

    perm_view_shippingaddress = permission_class.objects.filter(content_type__app_label='store',
                                                                content_type__model='shippingaddress',
                                                                codename='view_shippingaddress')

    ci_manager_permissions = chain(customer_permissions,
                                   order_permissions,
                                   orderitem_permissions,
                                   shippingaddress_permissions,
                                   perm_view_customer,
                                   perm_view_order,
                                   perm_view_orderitem,
                                   perm_view_shippingaddress,
                                   )

    ci_shipper_permissions = chain(perm_view_customer,
                                   perm_view_shippingaddress,
                                   )

    ci_customer_permissions = chain(perm_view_order,
                                    perm_view_orderitem,
                                    perm_view_shippingaddress,
                                    )

    my_groups_initialization_list = [
        {
            "name": "ci_manager",
            "permissions_list": ci_manager_permissions,
        },
        {
            "name": "ci_shipper",
            "permissions_list": ci_shipper_permissions,
        },
        {
            "name": "ci_customer",
            "permissions_list": ci_customer_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0002_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
